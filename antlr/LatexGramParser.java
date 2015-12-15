// Generated from LatexGram.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LatexGramParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.5.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, MUL=8, ADD=9, 
		SUB=10, DIV=11, NUM=12, ZERO=13, ONE=14, VAR=15, WS=16;
	public static final int
		RULE_s = 0, RULE_expr = 1, RULE_pack = 2, RULE_atom = 3;
	public static final String[] ruleNames = {
		"s", "expr", "pack", "atom"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'^'", "'('", "')'", "'['", "']'", "'{'", "'}'", null, "'+'", "'-'", 
		"'/'", null, "'0'", "'1'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, "MUL", "ADD", "SUB", "DIV", 
		"NUM", "ZERO", "ONE", "VAR", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LatexGram.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LatexGramParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class SContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public SContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterS(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitS(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitS(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SContext s() throws RecognitionException {
		SContext _localctx = new SContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_s);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class DivContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DIV() { return getToken(LatexGramParser.DIV, 0); }
		public DivContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterDiv(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitDiv(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitDiv(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AddContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(LatexGramParser.ADD, 0); }
		public AddContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterAdd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitAdd(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitAdd(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class SubContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode SUB() { return getToken(LatexGramParser.SUB, 0); }
		public SubContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterSub(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitSub(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitSub(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class MulContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(LatexGramParser.MUL, 0); }
		public MulContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterMul(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitMul(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitMul(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AtomicContext extends ExprContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public AtomicContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterAtomic(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitAtomic(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitAtomic(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class PowContext extends ExprContext {
		public List<PackContext> pack() {
			return getRuleContexts(PackContext.class);
		}
		public PackContext pack(int i) {
			return getRuleContext(PackContext.class,i);
		}
		public PowContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterPow(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitPow(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitPow(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class IMulContext extends ExprContext {
		public List<PackContext> pack() {
			return getRuleContexts(PackContext.class);
		}
		public PackContext pack(int i) {
			return getRuleContext(PackContext.class,i);
		}
		public IMulContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterIMul(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitIMul(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitIMul(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class PackedContext extends ExprContext {
		public PackContext pack() {
			return getRuleContext(PackContext.class,0);
		}
		public PackedContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterPacked(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitPacked(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitPacked(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				_localctx = new AtomicContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(11);
				atom();
				}
				break;
			case 2:
				{
				_localctx = new PackedContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(12);
				pack();
				}
				break;
			case 3:
				{
				_localctx = new PowContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(13);
				pack();
				setState(14);
				match(T__0);
				setState(15);
				pack();
				}
				break;
			case 4:
				{
				_localctx = new IMulContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(17);
				pack();
				setState(18);
				pack();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(36);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(34);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						_localctx = new DivContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(22);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(23);
						match(DIV);
						setState(24);
						expr(5);
						}
						break;
					case 2:
						{
						_localctx = new MulContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(25);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(26);
						match(MUL);
						setState(27);
						expr(4);
						}
						break;
					case 3:
						{
						_localctx = new SubContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(28);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(29);
						match(SUB);
						setState(30);
						expr(3);
						}
						break;
					case 4:
						{
						_localctx = new AddContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(31);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(32);
						match(ADD);
						setState(33);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(38);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class PackContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PackContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pack; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterPack(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitPack(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitPack(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PackContext pack() throws RecognitionException {
		PackContext _localctx = new PackContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_pack);
		try {
			setState(48);
			switch (_input.LA(1)) {
			case T__5:
			case NUM:
			case ZERO:
			case ONE:
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				atom();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(40);
				match(T__1);
				setState(41);
				expr(0);
				setState(42);
				match(T__2);
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 3);
				{
				setState(44);
				match(T__3);
				setState(45);
				expr(0);
				setState(46);
				match(T__4);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public TerminalNode NUM() { return getToken(LatexGramParser.NUM, 0); }
		public TerminalNode ZERO() { return getToken(LatexGramParser.ZERO, 0); }
		public TerminalNode ONE() { return getToken(LatexGramParser.ONE, 0); }
		public TerminalNode VAR() { return getToken(LatexGramParser.VAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).enterAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LatexGramListener ) ((LatexGramListener)listener).exitAtom(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LatexGramVisitor ) return ((LatexGramVisitor<? extends T>)visitor).visitAtom(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_atom);
		try {
			setState(58);
			switch (_input.LA(1)) {
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				match(NUM);
				}
				break;
			case ZERO:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				match(ZERO);
				}
				break;
			case ONE:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				match(ONE);
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 4);
				{
				setState(53);
				match(VAR);
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 5);
				{
				setState(54);
				match(T__5);
				setState(55);
				expr(0);
				setState(56);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 1:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\22?\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3"+
		"\27\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3%\n\3\f\3\16"+
		"\3(\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\63\n\4\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\5\5=\n\5\3\5\2\3\4\6\2\4\6\b\2\2G\2\n\3\2\2\2\4\26"+
		"\3\2\2\2\6\62\3\2\2\2\b<\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f\r\b\3\1\2"+
		"\r\27\5\b\5\2\16\27\5\6\4\2\17\20\5\6\4\2\20\21\7\3\2\2\21\22\5\6\4\2"+
		"\22\27\3\2\2\2\23\24\5\6\4\2\24\25\5\6\4\2\25\27\3\2\2\2\26\f\3\2\2\2"+
		"\26\16\3\2\2\2\26\17\3\2\2\2\26\23\3\2\2\2\27&\3\2\2\2\30\31\f\6\2\2\31"+
		"\32\7\r\2\2\32%\5\4\3\7\33\34\f\5\2\2\34\35\7\n\2\2\35%\5\4\3\6\36\37"+
		"\f\4\2\2\37 \7\f\2\2 %\5\4\3\5!\"\f\3\2\2\"#\7\13\2\2#%\5\4\3\4$\30\3"+
		"\2\2\2$\33\3\2\2\2$\36\3\2\2\2$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2"+
		"\2\'\5\3\2\2\2(&\3\2\2\2)\63\5\b\5\2*+\7\4\2\2+,\5\4\3\2,-\7\5\2\2-\63"+
		"\3\2\2\2./\7\6\2\2/\60\5\4\3\2\60\61\7\7\2\2\61\63\3\2\2\2\62)\3\2\2\2"+
		"\62*\3\2\2\2\62.\3\2\2\2\63\7\3\2\2\2\64=\7\16\2\2\65=\7\17\2\2\66=\7"+
		"\20\2\2\67=\7\21\2\289\7\b\2\29:\5\4\3\2:;\7\t\2\2;=\3\2\2\2<\64\3\2\2"+
		"\2<\65\3\2\2\2<\66\3\2\2\2<\67\3\2\2\2<8\3\2\2\2=\t\3\2\2\2\7\26$&\62"+
		"<";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}