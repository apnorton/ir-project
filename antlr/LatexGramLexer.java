// Generated from LatexGram.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LatexGramLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.5.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, MUL=8, ADD=9, 
		SUB=10, DIV=11, NUM=12, ZERO=13, ONE=14, VAR=15, WS=16;
	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "MUL", "ADD", 
		"SUB", "DIV", "NUM", "ZERO", "ONE", "VAR", "WS"
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


	public LatexGramLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "LatexGram.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\22\u00c6\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3"+
		"\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t>\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\6"+
		"\rG\n\r\r\r\16\rH\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00be\n\20\3\21\6\21\u00c1\n\21"+
		"\r\21\16\21\u00c2\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n"+
		"\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\5\3\2\62;\4\2C\\c|\5"+
		"\2\13\f\17\17\"\"\u00df\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2"+
		"\2\r-\3\2\2\2\17/\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27C\3\2"+
		"\2\2\31F\3\2\2\2\33J\3\2\2\2\35L\3\2\2\2\37\u00bd\3\2\2\2!\u00c0\3\2\2"+
		"\2#$\7`\2\2$\4\3\2\2\2%&\7*\2\2&\6\3\2\2\2\'(\7+\2\2(\b\3\2\2\2)*\7]\2"+
		"\2*\n\3\2\2\2+,\7_\2\2,\f\3\2\2\2-.\7}\2\2.\16\3\2\2\2/\60\7\177\2\2\60"+
		"\20\3\2\2\2\61>\7,\2\2\62\63\7^\2\2\63\64\7v\2\2\64\65\7k\2\2\65\66\7"+
		"o\2\2\66\67\7g\2\2\67>\7u\2\289\7^\2\29:\7e\2\2:;\7f\2\2;<\7q\2\2<>\7"+
		"v\2\2=\61\3\2\2\2=\62\3\2\2\2=8\3\2\2\2>\22\3\2\2\2?@\7-\2\2@\24\3\2\2"+
		"\2AB\7/\2\2B\26\3\2\2\2CD\7\61\2\2D\30\3\2\2\2EG\t\2\2\2FE\3\2\2\2GH\3"+
		"\2\2\2HF\3\2\2\2HI\3\2\2\2I\32\3\2\2\2JK\7\62\2\2K\34\3\2\2\2LM\7\63\2"+
		"\2M\36\3\2\2\2N\u00be\t\3\2\2OP\7^\2\2PQ\7c\2\2QR\7n\2\2RS\7r\2\2ST\7"+
		"j\2\2T\u00be\7c\2\2UV\7^\2\2VW\7d\2\2WX\7g\2\2XY\7v\2\2Y\u00be\7c\2\2"+
		"Z[\7^\2\2[\\\7f\2\2\\]\7g\2\2]^\7n\2\2^_\7v\2\2_\u00be\7c\2\2`a\7^\2\2"+
		"ab\7g\2\2bc\7r\2\2cd\7u\2\2de\7k\2\2ef\7n\2\2fg\7q\2\2g\u00be\7p\2\2h"+
		"i\7^\2\2ij\7|\2\2jk\7g\2\2kl\7v\2\2l\u00be\7c\2\2mn\7^\2\2no\7g\2\2op"+
		"\7v\2\2p\u00be\7c\2\2qr\7^\2\2rs\7v\2\2st\7j\2\2tu\7g\2\2uv\7v\2\2v\u00be"+
		"\7c\2\2wx\7^\2\2xy\7k\2\2yz\7q\2\2z{\7v\2\2{\u00be\7c\2\2|}\7^\2\2}~\7"+
		"m\2\2~\177\7c\2\2\177\u0080\7r\2\2\u0080\u0081\7r\2\2\u0081\u00be\7c\2"+
		"\2\u0082\u0083\7^\2\2\u0083\u0084\7n\2\2\u0084\u0085\7c\2\2\u0085\u0086"+
		"\7o\2\2\u0086\u0087\7d\2\2\u0087\u0088\7f\2\2\u0088\u00be\7c\2\2\u0089"+
		"\u008a\7^\2\2\u008a\u008b\7o\2\2\u008b\u00be\7w\2\2\u008c\u008d\7^\2\2"+
		"\u008d\u008e\7p\2\2\u008e\u00be\7w\2\2\u008f\u0090\7^\2\2\u0090\u0091"+
		"\7z\2\2\u0091\u00be\7k\2\2\u0092\u0093\7^\2\2\u0093\u0094\7r\2\2\u0094"+
		"\u00be\7k\2\2\u0095\u0096\7^\2\2\u0096\u0097\7t\2\2\u0097\u0098\7j\2\2"+
		"\u0098\u00be\7q\2\2\u0099\u009a\7^\2\2\u009a\u009b\7u\2\2\u009b\u009c"+
		"\7k\2\2\u009c\u009d\7i\2\2\u009d\u009e\7o\2\2\u009e\u00be\7c\2\2\u009f"+
		"\u00a0\7^\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7c\2\2\u00a2\u00be\7w\2\2"+
		"\u00a3\u00a4\7^\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7"+
		"\7u\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa\7q\2\2\u00aa"+
		"\u00be\7p\2\2\u00ab\u00ac\7^\2\2\u00ac\u00ad\7r\2\2\u00ad\u00ae\7j\2\2"+
		"\u00ae\u00be\7k\2\2\u00af\u00b0\7^\2\2\u00b0\u00b1\7e\2\2\u00b1\u00b2"+
		"\7j\2\2\u00b2\u00be\7k\2\2\u00b3\u00b4\7^\2\2\u00b4\u00b5\7r\2\2\u00b5"+
		"\u00b6\7u\2\2\u00b6\u00be\7k\2\2\u00b7\u00b8\7^\2\2\u00b8\u00b9\7q\2\2"+
		"\u00b9\u00ba\7o\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7i\2\2\u00bc\u00be"+
		"\7c\2\2\u00bdN\3\2\2\2\u00bdO\3\2\2\2\u00bdU\3\2\2\2\u00bdZ\3\2\2\2\u00bd"+
		"`\3\2\2\2\u00bdh\3\2\2\2\u00bdm\3\2\2\2\u00bdq\3\2\2\2\u00bdw\3\2\2\2"+
		"\u00bd|\3\2\2\2\u00bd\u0082\3\2\2\2\u00bd\u0089\3\2\2\2\u00bd\u008c\3"+
		"\2\2\2\u00bd\u008f\3\2\2\2\u00bd\u0092\3\2\2\2\u00bd\u0095\3\2\2\2\u00bd"+
		"\u0099\3\2\2\2\u00bd\u009f\3\2\2\2\u00bd\u00a3\3\2\2\2\u00bd\u00ab\3\2"+
		"\2\2\u00bd\u00af\3\2\2\2\u00bd\u00b3\3\2\2\2\u00bd\u00b7\3\2\2\2\u00be"+
		" \3\2\2\2\u00bf\u00c1\t\4\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2"+
		"\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5"+
		"\b\21\2\2\u00c5\"\3\2\2\2\7\2=H\u00bd\u00c2\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}