// Generated from C:/Users/karol/PycharmProjects/GP-antlr\TinyGP.g4 by ANTLR 4.12.0
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TinyGPParser}.
 */
public interface TinyGPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(TinyGPParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(TinyGPParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(TinyGPParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(TinyGPParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoopStatement(TinyGPParser.LoopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoopStatement(TinyGPParser.LoopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#conditionalStatement}.
	 * @param ctx the parse tree
	 */
	void enterConditionalStatement(TinyGPParser.ConditionalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#conditionalStatement}.
	 * @param ctx the parse tree
	 */
	void exitConditionalStatement(TinyGPParser.ConditionalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void enterCompoundStatement(TinyGPParser.CompoundStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void exitCompoundStatement(TinyGPParser.CompoundStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(TinyGPParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#assignmentStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(TinyGPParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#inputStatement}.
	 * @param ctx the parse tree
	 */
	void enterInputStatement(TinyGPParser.InputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#inputStatement}.
	 * @param ctx the parse tree
	 */
	void exitInputStatement(TinyGPParser.InputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#outputStatement}.
	 * @param ctx the parse tree
	 */
	void enterOutputStatement(TinyGPParser.OutputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#outputStatement}.
	 * @param ctx the parse tree
	 */
	void exitOutputStatement(TinyGPParser.OutputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(TinyGPParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(TinyGPParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(TinyGPParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(TinyGPParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(TinyGPParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(TinyGPParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(TinyGPParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(TinyGPParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(TinyGPParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(TinyGPParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(TinyGPParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(TinyGPParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(TinyGPParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(TinyGPParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGPParser#boolean}.
	 * @param ctx the parse tree
	 */
	void enterBoolean(TinyGPParser.BooleanContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGPParser#boolean}.
	 * @param ctx the parse tree
	 */
	void exitBoolean(TinyGPParser.BooleanContext ctx);
}