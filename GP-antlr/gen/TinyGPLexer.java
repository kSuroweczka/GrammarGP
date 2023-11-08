// Generated from C:/Users/karol/PycharmProjects/GP-antlr\TinyGP.g4 by ANTLR 4.12.0
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class TinyGPLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.12.0", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, NUMBER=2, WS=3, WHILE=4, IF=5, ELSE=6, INPUT=7, OUTPUT=8, TRUE=9, 
		FALSE=10, LEFTCURLY=11, RIGHTCURLY=12, LEFTPAREN=13, RIGHTPAREN=14, COMMA=15, 
		SEMICOLON=16, PLUSEQUAL=17, MINUSEQUAL=18, MULEQUAL=19, DIVIDEEQUAL=20, 
		PLUS=21, MINUS=22, MUL=23, DIVIDE=24, GREATER=25, LESS=26, LESSEQUAL=27, 
		MOREEQUAL=28, EQUALEQUAL=29, NOTEQUAL=30, EQUAL=31, AND=32, OR=33;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ID", "NUMBER", "WS", "WHILE", "IF", "ELSE", "INPUT", "OUTPUT", "TRUE", 
			"FALSE", "LEFTCURLY", "RIGHTCURLY", "LEFTPAREN", "RIGHTPAREN", "COMMA", 
			"SEMICOLON", "PLUSEQUAL", "MINUSEQUAL", "MULEQUAL", "DIVIDEEQUAL", "PLUS", 
			"MINUS", "MUL", "DIVIDE", "GREATER", "LESS", "LESSEQUAL", "MOREEQUAL", 
			"EQUALEQUAL", "NOTEQUAL", "EQUAL", "AND", "OR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'while'", "'if'", "'else'", "'input'", "'output'", 
			"'true'", "'false'", "'{'", "'}'", "'('", "')'", "','", "';'", "'+='", 
			"'-='", "'*='", "'/='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'<='", 
			"'>='", "'=='", "'!='", "'='", "'&&'", "'||'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ID", "NUMBER", "WS", "WHILE", "IF", "ELSE", "INPUT", "OUTPUT", 
			"TRUE", "FALSE", "LEFTCURLY", "RIGHTCURLY", "LEFTPAREN", "RIGHTPAREN", 
			"COMMA", "SEMICOLON", "PLUSEQUAL", "MINUSEQUAL", "MULEQUAL", "DIVIDEEQUAL", 
			"PLUS", "MINUS", "MUL", "DIVIDE", "GREATER", "LESS", "LESSEQUAL", "MOREEQUAL", 
			"EQUALEQUAL", "NOTEQUAL", "EQUAL", "AND", "OR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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


	public TinyGPLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "TinyGP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000!\u00b4\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0001\u0000\u0001"+
		"\u0000\u0005\u0000F\b\u0000\n\u0000\f\u0000I\t\u0000\u0001\u0001\u0004"+
		"\u0001L\b\u0001\u000b\u0001\f\u0001M\u0001\u0002\u0004\u0002Q\b\u0002"+
		"\u000b\u0002\f\u0002R\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b"+
		"\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001 \u0001"+
		" \u0001 \u0000\u0000!\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'"+
		"\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d"+
		";\u001e=\u001f? A!\u0001\u0000\u0004\u0002\u0000AZaz\u0003\u000009AZa"+
		"z\u0001\u000009\u0003\u0000\t\n\r\r  \u00b6\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000"+
		"\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001"+
		"\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000"+
		"\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000"+
		"\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001"+
		"\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001\u0000"+
		"\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000"+
		"\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?"+
		"\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0001C\u0001\u0000"+
		"\u0000\u0000\u0003K\u0001\u0000\u0000\u0000\u0005P\u0001\u0000\u0000\u0000"+
		"\u0007V\u0001\u0000\u0000\u0000\t\\\u0001\u0000\u0000\u0000\u000b_\u0001"+
		"\u0000\u0000\u0000\rd\u0001\u0000\u0000\u0000\u000fj\u0001\u0000\u0000"+
		"\u0000\u0011q\u0001\u0000\u0000\u0000\u0013v\u0001\u0000\u0000\u0000\u0015"+
		"|\u0001\u0000\u0000\u0000\u0017~\u0001\u0000\u0000\u0000\u0019\u0080\u0001"+
		"\u0000\u0000\u0000\u001b\u0082\u0001\u0000\u0000\u0000\u001d\u0084\u0001"+
		"\u0000\u0000\u0000\u001f\u0086\u0001\u0000\u0000\u0000!\u0088\u0001\u0000"+
		"\u0000\u0000#\u008b\u0001\u0000\u0000\u0000%\u008e\u0001\u0000\u0000\u0000"+
		"\'\u0091\u0001\u0000\u0000\u0000)\u0094\u0001\u0000\u0000\u0000+\u0096"+
		"\u0001\u0000\u0000\u0000-\u0098\u0001\u0000\u0000\u0000/\u009a\u0001\u0000"+
		"\u0000\u00001\u009c\u0001\u0000\u0000\u00003\u009e\u0001\u0000\u0000\u0000"+
		"5\u00a0\u0001\u0000\u0000\u00007\u00a3\u0001\u0000\u0000\u00009\u00a6"+
		"\u0001\u0000\u0000\u0000;\u00a9\u0001\u0000\u0000\u0000=\u00ac\u0001\u0000"+
		"\u0000\u0000?\u00ae\u0001\u0000\u0000\u0000A\u00b1\u0001\u0000\u0000\u0000"+
		"CG\u0007\u0000\u0000\u0000DF\u0007\u0001\u0000\u0000ED\u0001\u0000\u0000"+
		"\u0000FI\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000GH\u0001\u0000"+
		"\u0000\u0000H\u0002\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000"+
		"JL\u0007\u0002\u0000\u0000KJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000"+
		"\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\u0004\u0001"+
		"\u0000\u0000\u0000OQ\u0007\u0003\u0000\u0000PO\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000"+
		"\u0000ST\u0001\u0000\u0000\u0000TU\u0006\u0002\u0000\u0000U\u0006\u0001"+
		"\u0000\u0000\u0000VW\u0005w\u0000\u0000WX\u0005h\u0000\u0000XY\u0005i"+
		"\u0000\u0000YZ\u0005l\u0000\u0000Z[\u0005e\u0000\u0000[\b\u0001\u0000"+
		"\u0000\u0000\\]\u0005i\u0000\u0000]^\u0005f\u0000\u0000^\n\u0001\u0000"+
		"\u0000\u0000_`\u0005e\u0000\u0000`a\u0005l\u0000\u0000ab\u0005s\u0000"+
		"\u0000bc\u0005e\u0000\u0000c\f\u0001\u0000\u0000\u0000de\u0005i\u0000"+
		"\u0000ef\u0005n\u0000\u0000fg\u0005p\u0000\u0000gh\u0005u\u0000\u0000"+
		"hi\u0005t\u0000\u0000i\u000e\u0001\u0000\u0000\u0000jk\u0005o\u0000\u0000"+
		"kl\u0005u\u0000\u0000lm\u0005t\u0000\u0000mn\u0005p\u0000\u0000no\u0005"+
		"u\u0000\u0000op\u0005t\u0000\u0000p\u0010\u0001\u0000\u0000\u0000qr\u0005"+
		"t\u0000\u0000rs\u0005r\u0000\u0000st\u0005u\u0000\u0000tu\u0005e\u0000"+
		"\u0000u\u0012\u0001\u0000\u0000\u0000vw\u0005f\u0000\u0000wx\u0005a\u0000"+
		"\u0000xy\u0005l\u0000\u0000yz\u0005s\u0000\u0000z{\u0005e\u0000\u0000"+
		"{\u0014\u0001\u0000\u0000\u0000|}\u0005{\u0000\u0000}\u0016\u0001\u0000"+
		"\u0000\u0000~\u007f\u0005}\u0000\u0000\u007f\u0018\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0005(\u0000\u0000\u0081\u001a\u0001\u0000\u0000\u0000\u0082"+
		"\u0083\u0005)\u0000\u0000\u0083\u001c\u0001\u0000\u0000\u0000\u0084\u0085"+
		"\u0005,\u0000\u0000\u0085\u001e\u0001\u0000\u0000\u0000\u0086\u0087\u0005"+
		";\u0000\u0000\u0087 \u0001\u0000\u0000\u0000\u0088\u0089\u0005+\u0000"+
		"\u0000\u0089\u008a\u0005=\u0000\u0000\u008a\"\u0001\u0000\u0000\u0000"+
		"\u008b\u008c\u0005-\u0000\u0000\u008c\u008d\u0005=\u0000\u0000\u008d$"+
		"\u0001\u0000\u0000\u0000\u008e\u008f\u0005*\u0000\u0000\u008f\u0090\u0005"+
		"=\u0000\u0000\u0090&\u0001\u0000\u0000\u0000\u0091\u0092\u0005/\u0000"+
		"\u0000\u0092\u0093\u0005=\u0000\u0000\u0093(\u0001\u0000\u0000\u0000\u0094"+
		"\u0095\u0005+\u0000\u0000\u0095*\u0001\u0000\u0000\u0000\u0096\u0097\u0005"+
		"-\u0000\u0000\u0097,\u0001\u0000\u0000\u0000\u0098\u0099\u0005*\u0000"+
		"\u0000\u0099.\u0001\u0000\u0000\u0000\u009a\u009b\u0005/\u0000\u0000\u009b"+
		"0\u0001\u0000\u0000\u0000\u009c\u009d\u0005>\u0000\u0000\u009d2\u0001"+
		"\u0000\u0000\u0000\u009e\u009f\u0005<\u0000\u0000\u009f4\u0001\u0000\u0000"+
		"\u0000\u00a0\u00a1\u0005<\u0000\u0000\u00a1\u00a2\u0005=\u0000\u0000\u00a2"+
		"6\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005>\u0000\u0000\u00a4\u00a5\u0005"+
		"=\u0000\u0000\u00a58\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005=\u0000"+
		"\u0000\u00a7\u00a8\u0005=\u0000\u0000\u00a8:\u0001\u0000\u0000\u0000\u00a9"+
		"\u00aa\u0005!\u0000\u0000\u00aa\u00ab\u0005=\u0000\u0000\u00ab<\u0001"+
		"\u0000\u0000\u0000\u00ac\u00ad\u0005=\u0000\u0000\u00ad>\u0001\u0000\u0000"+
		"\u0000\u00ae\u00af\u0005&\u0000\u0000\u00af\u00b0\u0005&\u0000\u0000\u00b0"+
		"@\u0001\u0000\u0000\u0000\u00b1\u00b2\u0005|\u0000\u0000\u00b2\u00b3\u0005"+
		"|\u0000\u0000\u00b3B\u0001\u0000\u0000\u0000\u0004\u0000GMR\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}