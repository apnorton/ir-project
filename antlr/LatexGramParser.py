# Generated from LatexGram.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\22A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write(u"\33\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\7\3)\n\3\f\3\16\3,\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\5\4\67\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5?\n")
        buf.write(u"\5\3\5\2\3\4\6\2\4\6\b\2\2I\2\n\3\2\2\2\4\32\3\2\2\2")
        buf.write(u"\6\66\3\2\2\2\b>\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f")
        buf.write(u"\r\b\3\1\2\r\16\7\21\2\2\16\33\5\4\3\t\17\33\5\b\5\2")
        buf.write(u"\20\33\5\6\4\2\21\22\5\6\4\2\22\23\7\3\2\2\23\24\5\6")
        buf.write(u"\4\2\24\33\3\2\2\2\25\26\5\6\4\2\26\27\5\6\4\2\27\33")
        buf.write(u"\3\2\2\2\30\31\7\22\2\2\31\33\5\6\4\2\32\f\3\2\2\2\32")
        buf.write(u"\17\3\2\2\2\32\20\3\2\2\2\32\21\3\2\2\2\32\25\3\2\2\2")
        buf.write(u"\32\30\3\2\2\2\33*\3\2\2\2\34\35\f\7\2\2\35\36\7\r\2")
        buf.write(u"\2\36)\5\4\3\b\37 \f\6\2\2 !\7\n\2\2!)\5\4\3\7\"#\f\5")
        buf.write(u"\2\2#$\7\f\2\2$)\5\4\3\6%&\f\4\2\2&\'\7\13\2\2\')\5\4")
        buf.write(u"\3\5(\34\3\2\2\2(\37\3\2\2\2(\"\3\2\2\2(%\3\2\2\2),\3")
        buf.write(u"\2\2\2*(\3\2\2\2*+\3\2\2\2+\5\3\2\2\2,*\3\2\2\2-\67\5")
        buf.write(u"\b\5\2./\7\4\2\2/\60\5\4\3\2\60\61\7\5\2\2\61\67\3\2")
        buf.write(u"\2\2\62\63\7\6\2\2\63\64\5\4\3\2\64\65\7\7\2\2\65\67")
        buf.write(u"\3\2\2\2\66-\3\2\2\2\66.\3\2\2\2\66\62\3\2\2\2\67\7\3")
        buf.write(u"\2\2\28?\7\16\2\29?\7\20\2\2:;\7\b\2\2;<\5\4\3\2<=\7")
        buf.write(u"\t\2\2=?\3\2\2\2>8\3\2\2\2>9\3\2\2\2>:\3\2\2\2?\t\3\2")
        buf.write(u"\2\2\7\32(*\66>")
        return buf.getvalue()


class LatexGramParser ( Parser ):

    grammarFileName = "LatexGram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'^'", u"'('", u"')'", u"'['", u"']'", 
                     u"'{'", u"'}'", u"<INVALID>", u"'+'", u"'-'", u"'/'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"MUL", u"ADD", u"SUB", u"DIV", u"NUM", u"WS", u"VAR", 
                      u"BIG_OP", u"TRIG_OP" ]

    RULE_s = 0
    RULE_expr = 1
    RULE_pack = 2
    RULE_atom = 3

    ruleNames =  [ u"s", u"expr", u"pack", u"atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    MUL=8
    ADD=9
    SUB=10
    DIV=11
    NUM=12
    WS=13
    VAR=14
    BIG_OP=15
    TRIG_OP=16

    def __init__(self, input):
        super(LatexGramParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LatexGramParser.SContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LatexGramParser.ExprContext,0)


        def getRuleIndex(self):
            return LatexGramParser.RULE_s

        def enterRule(self, listener):
            if hasattr(listener, "enterS"):
                listener.enterS(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitS"):
                listener.exitS(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitS"):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = LatexGramParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LatexGramParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatexGramParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(LatexGramParser.ExprContext, self).copyFrom(ctx)


    class DivContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.DivContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.ExprContext,i)

        def DIV(self):
            return self.getToken(LatexGramParser.DIV, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDiv"):
                listener.enterDiv(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDiv"):
                listener.exitDiv(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitDiv"):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.AddContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.ExprContext,i)

        def ADD(self):
            return self.getToken(LatexGramParser.ADD, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAdd"):
                listener.enterAdd(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAdd"):
                listener.exitAdd(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAdd"):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.SubContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.ExprContext,i)

        def SUB(self):
            return self.getToken(LatexGramParser.SUB, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterSub"):
                listener.enterSub(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSub"):
                listener.exitSub(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSub"):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.MulContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.ExprContext,i)

        def MUL(self):
            return self.getToken(LatexGramParser.MUL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMul"):
                listener.enterMul(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMul"):
                listener.exitMul(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMul"):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class BigOpContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.BigOpContext, self).__init__(parser)
            self.copyFrom(ctx)

        def BIG_OP(self):
            return self.getToken(LatexGramParser.BIG_OP, 0)
        def expr(self):
            return self.getTypedRuleContext(LatexGramParser.ExprContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBigOp"):
                listener.enterBigOp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBigOp"):
                listener.exitBigOp(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitBigOp"):
                return visitor.visitBigOp(self)
            else:
                return visitor.visitChildren(self)


    class AtomicContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.AtomicContext, self).__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(LatexGramParser.AtomContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAtomic"):
                listener.enterAtomic(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomic"):
                listener.exitAtomic(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAtomic"):
                return visitor.visitAtomic(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.PowContext, self).__init__(parser)
            self.copyFrom(ctx)

        def pack(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.PackContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.PackContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterPow"):
                listener.enterPow(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPow"):
                listener.exitPow(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPow"):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class TrigContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.TrigContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TRIG_OP(self):
            return self.getToken(LatexGramParser.TRIG_OP, 0)
        def pack(self):
            return self.getTypedRuleContext(LatexGramParser.PackContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterTrig"):
                listener.enterTrig(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTrig"):
                listener.exitTrig(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitTrig"):
                return visitor.visitTrig(self)
            else:
                return visitor.visitChildren(self)


    class IMulContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.IMulContext, self).__init__(parser)
            self.copyFrom(ctx)

        def pack(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LatexGramParser.PackContext)
            else:
                return self.getTypedRuleContext(LatexGramParser.PackContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIMul"):
                listener.enterIMul(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIMul"):
                listener.exitIMul(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitIMul"):
                return visitor.visitIMul(self)
            else:
                return visitor.visitChildren(self)


    class PackedContext(ExprContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.ExprContext)
            super(LatexGramParser.PackedContext, self).__init__(parser)
            self.copyFrom(ctx)

        def pack(self):
            return self.getTypedRuleContext(LatexGramParser.PackContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterPacked"):
                listener.enterPacked(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPacked"):
                listener.exitPacked(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPacked"):
                return visitor.visitPacked(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LatexGramParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = LatexGramParser.BigOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 11
                self.match(LatexGramParser.BIG_OP)
                self.state = 12
                self.expr(7)
                pass

            elif la_ == 2:
                localctx = LatexGramParser.AtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.atom()
                pass

            elif la_ == 3:
                localctx = LatexGramParser.PackedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.pack()
                pass

            elif la_ == 4:
                localctx = LatexGramParser.PowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.pack()
                self.state = 16
                self.match(LatexGramParser.T__0)
                self.state = 17
                self.pack()
                pass

            elif la_ == 5:
                localctx = LatexGramParser.IMulContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.pack()
                self.state = 20
                self.pack()
                pass

            elif la_ == 6:
                localctx = LatexGramParser.TrigContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(LatexGramParser.TRIG_OP)
                self.state = 23
                self.pack()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LatexGramParser.DivContext(self, LatexGramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        self.match(LatexGramParser.DIV)
                        self.state = 28
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = LatexGramParser.MulContext(self, LatexGramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        self.match(LatexGramParser.MUL)
                        self.state = 31
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = LatexGramParser.SubContext(self, LatexGramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        self.match(LatexGramParser.SUB)
                        self.state = 34
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = LatexGramParser.AddContext(self, LatexGramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 36
                        self.match(LatexGramParser.ADD)
                        self.state = 37
                        self.expr(3)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class PackContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LatexGramParser.PackContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(LatexGramParser.AtomContext,0)


        def expr(self):
            return self.getTypedRuleContext(LatexGramParser.ExprContext,0)


        def getRuleIndex(self):
            return LatexGramParser.RULE_pack

        def enterRule(self, listener):
            if hasattr(listener, "enterPack"):
                listener.enterPack(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPack"):
                listener.exitPack(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPack"):
                return visitor.visitPack(self)
            else:
                return visitor.visitChildren(self)




    def pack(self):

        localctx = LatexGramParser.PackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pack)
        try:
            self.state = 52
            token = self._input.LA(1)
            if token in [LatexGramParser.T__5, LatexGramParser.NUM, LatexGramParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.atom()

            elif token in [LatexGramParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(LatexGramParser.T__1)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(LatexGramParser.T__2)

            elif token in [LatexGramParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(LatexGramParser.T__3)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(LatexGramParser.T__4)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LatexGramParser.AtomContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatexGramParser.RULE_atom

     
        def copyFrom(self, ctx):
            super(LatexGramParser.AtomContext, self).copyFrom(ctx)



    class AtmExprContext(AtomContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.AtomContext)
            super(LatexGramParser.AtmExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LatexGramParser.ExprContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAtmExpr"):
                listener.enterAtmExpr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtmExpr"):
                listener.exitAtmExpr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAtmExpr"):
                return visitor.visitAtmExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtmVarContext(AtomContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.AtomContext)
            super(LatexGramParser.AtmVarContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(LatexGramParser.VAR, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAtmVar"):
                listener.enterAtmVar(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtmVar"):
                listener.exitAtmVar(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAtmVar"):
                return visitor.visitAtmVar(self)
            else:
                return visitor.visitChildren(self)


    class AtmNumContext(AtomContext):

        def __init__(self, parser, ctx): # actually a LatexGramParser.AtomContext)
            super(LatexGramParser.AtmNumContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(LatexGramParser.NUM, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAtmNum"):
                listener.enterAtmNum(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtmNum"):
                listener.exitAtmNum(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAtmNum"):
                return visitor.visitAtmNum(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = LatexGramParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 60
            token = self._input.LA(1)
            if token in [LatexGramParser.NUM]:
                localctx = LatexGramParser.AtmNumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(LatexGramParser.NUM)

            elif token in [LatexGramParser.VAR]:
                localctx = LatexGramParser.AtmVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(LatexGramParser.VAR)

            elif token in [LatexGramParser.T__5]:
                localctx = LatexGramParser.AtmExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(LatexGramParser.T__5)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(LatexGramParser.T__6)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




