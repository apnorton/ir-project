"""
Using Visitor. Customized visitor walking down the tree and do calculation at
certain tree stage and eventually return result from the entry call.
"""
import os
import sys
import shutil
from antlr4 import *
from antlr4.InputStream import InputStream


from LatexGramLexer import LatexGramLexer
from LatexGramParser import  LatexGramParser
from LatexGramVisitor import LatexGramVisitor


class SymbolVisitor(LatexGramVisitor):
  def getSubtree(self, ctx):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))
    return left+right

  def visitAtmNum(self, ctx):
    return [str(ctx.NUM().getText())]

  def visitAtmVar(self, ctx):
    return [str(ctx.VAR().getText())]

  def visitAdd(self, ctx):
    return self.getSubtree(ctx)

  def visitSub(self, ctx):
    return self.getSubtree(ctx) 

  def visitDiv(self, ctx):
    return self.getSubtree(ctx)

  def visitPow(self, ctx):
    left = self.visit(ctx.pack(0))
    right = self.visit(ctx.pack(1))
    return left+right

  def visitTrig(self, ctx):
    return self.visit(ctx.pack())

  def visitBigOp(self, ctx):
    return self.visit(ctx.expr())

  def visitMul(self, ctx):
    return self.getSubtree(ctx)

  def visitIMul(self, ctx):
    left = self.visit(ctx.pack(0))
    right = self.visit(ctx.pack(1))
    return left+right

  def visitPack(self, ctx):
    if (ctx.expr() is not None):
      return self.visit(ctx.expr())
    else:
      return self.visit(ctx.atom())

  def visitAtmExpr(self, ctx):
    return self.visit(ctx.expr())

class EvalVisitor(LatexGramVisitor):
  def getSubtree(self, ctx, t):
    left = self.visit(ctx.expr(0))
    for l in left:
      l.append(t)
    right = self.visit(ctx.expr(1))
    for l in right:
      l.append(t)

    return left+right

  def visitAdd(self, ctx):
    return self.getSubtree(ctx, '+')

  def visitSub(self, ctx):
    return self.getSubtree(ctx, '-')

  def visitDiv(self, ctx):
    return self.getSubtree(ctx, '/')

  def visitPow(self, ctx):
    left = self.visit(ctx.pack(0))
    for l in left:
      l.append('^')
    right = self.visit(ctx.pack(1))
    for l in right:
      l.append('^')

    return left+right

  def visitTrig(self, ctx):
    lst = self.visit(ctx.pack())
    for l in lst:
      l.append('TRIG')
    return lst

  def visitBigOp(self, ctx):
    lst = self.visit(ctx.expr())
    for l in lst:
      l.append('BIG_OP')
    return lst

  def visitMul(self, ctx):
    return self.getSubtree(ctx, '*')

  def visitIMul(self, ctx):
    left = self.visit(ctx.pack(0))
    for l in left:
      l.append('*')
    right = self.visit(ctx.pack(1))
    for l in right:
      l.append('*')

    return left+right

  def visitPack(self, ctx):
    if (ctx.expr() is not None):
      return self.visit(ctx.expr())
    else:
      return self.visit(ctx.atom())

  def visitAtmNum(self, ctx):
    return [['NUM']]

  def visitAtmVar(self, ctx):
    return [['VAR']]

  def visitAtmExpr(self, ctx):
    return self.visit(ctx.expr())

# given latex string, returns the leaf-root paths
def getLeafRoots(s):
  input_stream = InputStream(s)

  lexer = LatexGramLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = LatexGramParser(token_stream)
  tree = parser.s()
  visitor = EvalVisitor()
  result = visitor.visit(tree)

  return result

def getSymbols(s):
  input_stream = InputStream(s)

  lexer = LatexGramLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = LatexGramParser(token_stream)
  tree = parser.s()
  visitor = SymbolVisitor()
  return visitor.visit(tree)

def addIndex(eqnId, path):
  directory = '../index/' + '/'.join(path)
  if not os.path.exists(directory):
    os.makedirs(directory)
  open(directory + '/' + str(eqnId), 'w')


def computeSymbolScore(q, d):
  q_symbols = set(getSymbols(q))
  d_symbols = set(getSymbols(d))

  qL = len(q_symbols)
  overlap = len(q_symbols.intersection(d_symbols))

  return float(overlap) / qL

def search(q, docs):
  print '\n--------'
  paths = getLeafRoots(q)

  print 'Search String: ', q

  toReturn = {}
  for p in paths:
    for i in range(1, len(p)+1):
      currResults = set()
      directory = '../index/' + '/'.join(p[:i])
      for rt, b, files in os.walk(directory):
        for r in files:
          currResults.add(r)

      for r in currResults:
        toReturn[int(r)] = toReturn.get(int(r), 0) + i
        toReturn[int(r)] += computeSymbolScore(q, docs[int(r)])

  for r, p in sorted(toReturn.items(), key=lambda k: k[1], reverse=True):
    print docs[r], " with priority ", p

if __name__ == '__main__':
  shutil.rmtree('../index/', ignore_errors=True)
  docs = {}
  with open('../data/eqns.txt') as f:
    lines = f.read().splitlines()

    i = 0
    for l in lines:
      print l, ":", i
      paths = getLeafRoots(l)
      for p in paths:
        addIndex(i, p)
      docs[i] = l
      i+=1
  
  search('\int x^3', docs)
  search('3+x+y', docs)
  search('z+x+y', docs)
  search('a+b', docs)
  search('(a+b)', docs)
  search('\sin(a)', docs)
  search('a', docs)
