"""
Using Visitor. Customized visitor walking down the tree and do calculation at
certain tree stage and eventually return result from the entry call.
"""
import os
import sys
from antlr4 import *
from antlr4.InputStream import InputStream


from LatexGramLexer import LatexGramLexer
from LatexGramParser import  LatexGramParser
from LatexGramVisitor import LatexGramVisitor


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

def addIndex(eqnId, path):
  directory = '../index/' + '/'.join(path)
  if not os.path.exists(directory):
    os.makedirs(directory)
  open(directory + '/' + str(eqnId), 'w')

if __name__ == '__main__':
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
  

  print 
  print '--------'
  mystr = "3+a+b"
  paths = getLeafRoots(mystr)

  print 'Search String: ', mystr

  toReturn = {}
  for p in paths:
    directory = '../index/' + '/'.join(p)
    for a, b, files in os.walk(directory):
      for r in files:
        toReturn[int(r)] = toReturn.get(int(r), 0) + 1
#    if os.path.exists(directory):
#      results = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]
#

  for r in toReturn:
    print docs[r], " with priority ", toReturn[r]
      
  print 
  print '--------'
  mystr = "a+b"
  paths = getLeafRoots(mystr)

  print 'Search String: ', mystr

  toReturn = {}
  for p in paths:
    directory = '../index/' + '/'.join(p)
    for a, b, files in os.walk(directory):
      for r in files:
        toReturn[int(r)] = toReturn.get(int(r), 0) + 1
#    if os.path.exists(directory):
#      results = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]
#

  for r in toReturn:
    print docs[r], " with priority ", toReturn[r]
      
