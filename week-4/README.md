# CRYPTO P&L TRACKER

#### Video Demo:  <[URL HERE](https://www.youtube.com/watch?v=XRrx9icy-aQ)>

#### Description:

## The Problem

This project comes from my own problem where I realized it's very hard to keep track of all my crypto positions. They're often spread across different exchanges, apps, wallets, etc.

I personally tried using spreadsheets before, but I had to update the prices manually, which wasn't a good solution either.

That's why I built this tool, so everyone could keep track of their crypto portfolio all in one place.

So what does it actually do?

## The Solution

It's pretty simple. Every time you buy or sell a crypto, just log it in the tracker.

If it's your first time using it, the system will automatically create a new CSV file for you. It will log all the position information, including total holdings, average entry price, position balance, and today's price.

If you've already used it before, your positions will automatically be updated. The system will then use that information to calculate your overall portfolio ROI.

Everything stays up to date thanks to the CoinGecko API.

## The Files

In this project, I have three main files:

1. **project.py**: This file contains the main source code of the project. It includes five main functions: `main()`, `checker()`, `buyAmount()`, `sellAmount()`, and `getPrice()`.

2. **test_project.py**: This file is used to test different possible cases for each function to make sure the project can handle all scenarios correctly.

3. **Crypto P&L Tracker.csv**: This file stores and updates all user positions.

## How the Functions Work

### 1. main()

`main()` handles the overall logic of the project. It decides the flow of the program, how different cases are handled, and how positions are updated and printed out for users.

### 2. checker()

The role of `checker()` is to identify the user's action, whether they buy, sell, do both, or simply want to check their balance for the day.

This helps sort users' actions first, which makes handling different cases inside `main()` much easier.

### 3. buyAmount()

`buyAmount()` receives information about users' buy orders. This includes which crypto they bought and how much they bought.

This function plays an important role because it makes sure users not only enter the correct information, but also enter it in the right format.

Only then can `main()` receive the correct data to continue updating the CSV file and calculating ROI afterward.

The function then returns three values to `main()`: the crypto ID, the entry price, and how much the user holds after buying.

### 4. sellAmount()

`sellAmount()` is quite similar to `buyAmount()`, but it handles sell orders instead.

It also takes care of two key cases that are different from buy orders:

* Users are not allowed to sell more than their balance.
* Selling does not affect the entry price.

The function then returns two values to `main()`: the crypto ID and how much the user holds after selling.

### 5. getPrice()

Since I want this tracker to stay up to date every time users use it, there are many situations where the program needs to fetch the latest market price. That's why I decided to build a separate function for it.

`getPrice()` receives a crypto ID as input, then returns the current price after requesting data from the CoinGecko API.

That way, we can always get fresh prices every time we use this tracker.

## Design Choices

The reason why I chose to build it this way is because:

### 1. Minimal user input

I want to minimize user input as much as possible. Users only need to input their orders. All the management and calculations are handled by the system.

### 2. Why I chose CoinGecko API

I chose CoinGecko API because:

* It's free. Anyone can create an API key and use it. A free Demo account has around 100 calls per minute, which is way more than enough for this project.
* There's no need for manual price updates anymore.

### 3. Why I chose CSV

When thinking about ways to manage a user database, many options came to mind, including JSON and classes. However, I chose CSV because:

* It's easy to create and update. In the end, each user only needs one file to manage all their positions, so the updating process is not too complicated.
* The readability of a CSV file is much better than a JSON file when displaying information to users. I can't imagine trying to read my positions from one very long line of text.
* If we have more users in the future, it's very easy to manage the database. We can simply identify the user at the beginning and only update their CSV file. In the worst case, if something happens to one user, other users won't be affected.

### 4. Why I calculate ROI this way

There are actually two ways to calculate ROI.

The first way is by using the principal capital and today's value. The second way is by calculating it based on price.

I actually used the first approach in the beginning, but I soon realized that it lacked a lot of useful information for users. They wouldn't know how much they hold, what their entry price is, and other important details.

Most people check today's price when they look at the market, so calculating based on price makes much more sense, imo.

Users won't have to think too much, and it's easier to digest all the key information.

## Future Improvements

There are a few things I want to improve in the future:

1. **More users**: More people will be able to use the tracker, and each user will have their own separate CSV file.

2. **Order history**: All user orders will be saved in a history section so they can check them whenever they want.

3. **Historical P&L Chart**: This will show users' P&L across different timeframes, from weekly and monthly to quarterly and yearly.

4. **AI Analysis**: Scrape market data for each crypto every day, then generate a detailed analysis with supporting sources and numbers.