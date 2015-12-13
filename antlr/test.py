import sys
from antlr4 import *
from TLexer import TLexer
from TParser import TParser
from TVisitor import TVisitor
from TListener import TListener

class MyVisitor(TVisitor):
  def visitMul(self, ctx):
    return self.visit(ctx.e(0)) * self.visit(ctx.e(1))
  
  def visitAdd(self, ctx):
    print "hey"
    print dir(ctx)
    return self.visit(ctx.e(0)) + self.visit(ctx.e(1))
  
  def visitInt(self, ctx):
    print "hey"
    return int(ctx.INT().getText())

  def visitSub(self, ctx):
    print "hey"
    return self.visit(ctx.e(0)) - self.visit(ctx.e(1))
    
  def visitDiv(self, ctx):
    print "hey"
    return self.visit(ctx.e(0)) // self.visit(ctx.e(1))

class TPrinter(TListener):
  def exitR(self, ctx):
    print 'hey'

def print_tree(tree, indent):
  print '{0}{1}'.format('  '*indent, tree.text)
  for child in tree.getChildren():
    print_tree(child, indent+1)

def main(argv):
  s = FileStream(argv[1])
  lexer = TLexer(s)
  stream = CommonTokenStream(lexer)
  parser = TParser(stream)
  tree = parser.r()

  print tree.toStringTree(recog=parser)

  visitor = TVisitor()
  result = visitor.visit(tree)
  print 'result = ', result

if __name__ == '__main__':
  main(sys.argv)
