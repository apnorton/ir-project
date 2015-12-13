"""
Using Visitor. Customized visitor walking down the tree and do calculation at
certain tree stage and eventually return result from the entry call.
"""
import sys
from antlr4 import *
from antlr4.InputStream import InputStream


from LatexGramLexer import LatexGramLexer
from LatexGramParser import  LatexGramParser
from LatexGramVisitor import LatexGramVisitor


class EvalVisitor(LatexGramVisitor):
    def getSubtree(self, ctx, t):
        left = self.visit(ctx.e(0))
        for l in left:
          l.append(t.getText())
        right = self.visit(ctx.e(1))
        for l in right:
          l.append(t.getText())

        return left+right

    def visitMul(self, ctx):
        r = self.getSubtree(ctx, ctx.MUL())
        return r

    def visitAdd(self, ctx):
        r = self.getSubtree(ctx, ctx.ADD())
        return r

    def visitInt(self, ctx):
        return [[ctx.INT().getText()]]

    def visitVar(self, ctx):
        return [[ctx.VAR().getText()]]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = LatexGramLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LatexGramParser(token_stream)
    tree = parser.s()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    visitor = EvalVisitor()
    result = visitor.visit(tree)
    print "result=", result
