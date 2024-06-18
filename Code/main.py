from fecth_data import fetch_news, fetch_stock_data
from calculations import calculate_max_drawdown, calculate_portfolio_metrics, calculate_sharpe_ratio, plot_signals
from sentiment import aggregate_sentiment_scores, generate_trading_signals, calculate_sentiment_scores
from simulate_trade import simulate_trades

def final(ticker, rate, intial):
    # Fetch stock data
    stock_data = fetch_stock_data(ticker)
    # Fetch news data
    news_data = fetch_news(ticker)
    # Calculate sentiment scores
    news_data_with_scores = calculate_sentiment_scores(news_data)
    # Aggregate sentiment scores by date
    sentiment_summary = aggregate_sentiment_scores(news_data_with_scores)
    # Generate trading signals
    trading_signals = generate_trading_signals(sentiment_summary)
    # Simulate trades
    print("\nSimulating trades...")
    portfolio = simulate_trades(stock_data, trading_signals, intial)
    # Calculate portfolio metrics
    total_trades, win_percentage, total_profit = calculate_portfolio_metrics(portfolio)
    # Print the portfolio
    print(portfolio)
    print(f"\nInitial capital: ${intial}")
    print(f"Total Trades: {total_trades}")
    print(f"Win Percentage: {win_percentage:.2f}%")
    print(f"Total Portfolio Returns: ${total_profit:.2f}")
    print(f"Sharpe ratio:{calculate_sharpe_ratio(portfolio, rate)}")
    print(f"Max drawdown: {calculate_max_drawdown(portfolio)}")
    # Plot buy and sell signals
    plot_signals(stock_data, portfolio, ticker)
    
    
final("MSFT",0.01, 100)