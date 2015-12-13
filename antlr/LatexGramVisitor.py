# Generated from LatexGram.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by LatexGramParser.

class LatexGramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatexGramParser#s.
    def visitS(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#Add.
    def visitAdd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#Mult.
    def visitMult(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#Var.
    def visitVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexGramParser#Int.
    def visitInt(self, ctx):
        return self.visitChildren(ctx)


