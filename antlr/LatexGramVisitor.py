# Generated from LatexGram.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by LatexGramParser.

class LatexGramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatexGramParser#s.
    def visitS(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#add.
    def visitAdd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#div.
    def visitDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#sub.
    def visitSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#Mul.
    def visitMul(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#atomic.
    def visitAtomic(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#pow.
    def visitPow(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#iMul.
    def visitIMul(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#packed.
    def visitPacked(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#pack.
    def visitPack(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#atom.
    def visitAtom(self, ctx):
        return self.visitChildren(ctx)


