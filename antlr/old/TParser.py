# Generated from T by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\n\36\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\13\n\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\31\n")
        buf.write(u"\2\f\2\16\2\34\13\2\3\2\2\3\2\3\2\2\2!\2\n\3\2\2\2\4")
        buf.write(u"\5\b\2\1\2\5\6\7\3\2\2\6\7\5\2\2\2\7\b\7\4\2\2\b\13\3")
        buf.write(u"\2\2\2\t\13\7\n\2\2\n\4\3\2\2\2\n\t\3\2\2\2\13\32\3\2")
        buf.write(u"\2\2\f\r\f\b\2\2\r\16\7\5\2\2\16\31\5\2\2\t\17\20\f\7")
        buf.write(u"\2\2\20\21\7\6\2\2\21\31\5\2\2\b\22\23\f\6\2\2\23\24")
        buf.write(u"\7\7\2\2\24\31\5\2\2\7\25\26\f\5\2\2\26\27\7\b\2\2\27")
        buf.write(u"\31\5\2\2\6\30\f\3\2\2\2\30\17\3\2\2\2\30\22\3\2\2\2")
        buf.write(u"\30\25\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2")
        buf.write(u"\2\2\33\3\3\2\2\2\34\32\3\2\2\2\5\n\30\32")
        return buf.getvalue()


class TParser ( Parser ):

    grammarFileName = "T"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"'*'", u"'+'", u"'/'", 
                     u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"MUL", 
                      u"ADD", u"DIV", u"SUB", u"WS", u"INT" ]

    RULE_r = 0

    ruleNames =  [ u"r" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    MUL=3
    ADD=4
    DIV=5
    SUB=6
    WS=7
    INT=8

    def __init__(self, input):
        super(TParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TParser.RContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TParser.RULE_r

     
        def copyFrom(self, ctx):
            super(TParser.RContext, self).copyFrom(ctx)


    class AddContext(RContext):

        def __init__(self, parser, ctx): # actually a TParser.RContext)
            super(TParser.AddContext, self).__init__(parser)
            self.copyFrom(ctx)

        def r(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TParser.RContext)
            else:
                return self.getTypedRuleContext(TParser.RContext,i)

        def ADD(self):
            return self.getToken(TParser.ADD, 0)

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


    class DivContext(RContext):

        def __init__(self, parser, ctx): # actually a TParser.RContext)
            super(TParser.DivContext, self).__init__(parser)
            self.copyFrom(ctx)

        def r(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TParser.RContext)
            else:
                return self.getTypedRuleContext(TParser.RContext,i)

        def DIV(self):
            return self.getToken(TParser.DIV, 0)

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


    class GroupContext(RContext):

        def __init__(self, parser, ctx): # actually a TParser.RContext)
            super(TParser.GroupContext, self).__init__(parser)
            self.copyFrom(ctx)

        def r(self):
            return self.getTypedRuleContext(TParser.RContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterGroup"):
                listener.enterGroup(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGroup"):
                listener.exitGroup(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitGroup"):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(RContext):

        def __init__(self, parser, ctx): # actually a TParser.RContext)
            super(TParser.SubContext, self).__init__(parser)
            self.copyFrom(ctx)

        def r(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TParser.RContext)
            else:
                return self.getTypedRuleContext(TParser.RContext,i)

        def SUB(self):
            return self.getToken(TParser.SUB, 0)

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


    class MulContext(RContext):

        def __init__(self, parser, ctx): # actually a TParser.RContext)
            super(TParser.MulContext, self).__init__(parser)
            self.copyFrom(ctx)

        def r(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TParser.RContext)
            else:
                return self.getTypedRuleContext(TParser.RContext,i)

        def MUL(self):
            return self.getToken(TParser.MUL, 0)

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


    class IntContext(RContext):

        def __init__(self, parser, ctx): # actually a TParser.RContext)
            super(TParser.IntContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TParser.INT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterInt"):
                listener.enterInt(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInt"):
                listener.exitInt(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitInt"):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def r(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TParser.RContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_r, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            token = self._input.LA(1)
            if token in [TParser.T__0]:
                localctx = TParser.GroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(TParser.T__0)
                self.state = 4
                self.r(0)
                self.state = 5
                self.match(TParser.T__1)

            elif token in [TParser.INT]:
                localctx = TParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(TParser.INT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = TParser.MulContext(self, TParser.RContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 10
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 11
                        self.match(TParser.MUL)
                        self.state = 12
                        self.r(7)
                        pass

                    elif la_ == 2:
                        localctx = TParser.AddContext(self, TParser.RContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 13
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 14
                        self.match(TParser.ADD)
                        self.state = 15
                        self.r(6)
                        pass

                    elif la_ == 3:
                        localctx = TParser.DivContext(self, TParser.RContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 16
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 17
                        self.match(TParser.DIV)
                        self.state = 18
                        self.r(5)
                        pass

                    elif la_ == 4:
                        localctx = TParser.SubContext(self, TParser.RContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_r)
                        self.state = 19
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 20
                        self.match(TParser.SUB)
                        self.state = 21
                        self.r(4)
                        pass

             
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.r_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def r_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




