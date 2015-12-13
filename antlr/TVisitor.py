# Generated from T by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by TParser.

class TVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TParser#Add.
    def visitAdd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TParser#Div.
    def visitDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TParser#Group.
    def visitGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TParser#Sub.
    def visitSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TParser#Mul.
    def visitMul(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TParser#Int.
    def visitInt(self, ctx):
        return self.visitChildren(ctx)


