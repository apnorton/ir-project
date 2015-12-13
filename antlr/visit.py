"""
Using Visitor. Customized visitor walking down the tree and do calculation at
certain tree stage and eventually return result from the entry call.
"""
import sys
from antlr4 import *
from antlr4.InputStream import InputStream


from LExprLexer import LExprLexer
from LExprParser import  LExprParser
from LExprVisitor import LExprVisitor


class EvalVisitor(LExprVisitor):
    def getSubtree(self, ctx, t):
        left = self.visit(ctx.e(0))
        for l in left:
          l.append(t.getText())
        right = self.visit(ctx.e(1))
        for l in right:
          l.append(t.getText())

        return left+right

    def visitMult(self, ctx):
        r = self.getSubtree(ctx, ctx.MULT())
        return r

    def visitAdd(self, ctx):
        r = self.getSubtree(ctx, ctx.ADD())
        return r

    def visitInt(self, ctx):
        return [[ctx.INT().getText()]]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = LExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LExprParser(token_stream)
    tree = parser.s()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    visitor = EvalVisitor()
    result = visitor.visit(tree)
    print "result=", result
