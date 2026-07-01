# Last Month Was an Incredible Month

Last month was an incredible month for me.

I started this journey without a single coding skill, and here I am today. I built my own project and earned the CS50 certificate, which is the first coding certificate I've ever received.

If you had asked me back on May 22, when I wrote my very first tweet about this journey, I would never have imagined I could come this far, this fast.

## Let Me Tell You About My Final Project

I actually came up with this project because it solves a problem I've had for a long time. I always struggled to manage all my crypto orders and positions because everything was so fragmented. My trades were scattered across different platforms, and it was difficult to know exactly how my portfolio was performing.

That's why I built the **Crypto P&L Tracker**. The goal is simple: help people manage their entire crypto portfolio in one place with real-time price updates.

## How Does It Work?

Pretty simple.

### Step 1

Every time you buy or sell a token, log the transaction into the tracker.

### Step 2

That's it.

The tracker automatically calculates the average entry price, the performance of each position, and your overall portfolio ROI. Whenever you want to see how your portfolio is doing, just ask the tracker to display it.

Thanks to the CoinGecko API, all token prices are updated in real time.

I chose CoinGecko because even the free API offers 100 requests per minute, which is more than enough for this use case.

## Project Structure

I divided the project into five key functions:

- **`main()`**
  - Handles the core logic
  - Calculates average prices
  - Computes the overall portfolio ROI

- **`checker()`**
  - Validates and filters user actions

- **`buyAmount()`**
  - Processes buy orders, including edge cases

- **`sellAmount()`**
  - Similar to `buyAmount()`, but for sell orders

- **`getPrice()`**
  - Fetches real-time token prices from the CoinGecko API

## The Biggest Challenge

If there was one difficult part of building this project, it was definitely time management.

I still have a full-time job, so finding time to code wasn't easy. Fortunately, I had a day off during the final week of CS50, and I spent the entire day coding. That was how I managed to finish the project on time.

More importantly, this project made me realize how much I genuinely enjoy coding and solving problems. I haven't felt this level of passion and curiosity about learning in a long time.

## Looking Ahead

I know this is still a very small milestone. Compared to the thousands of developers out there, I'm probably at the level of a second-year CS student.

But I always remind myself that everyone has to start somewhere.

I can become whoever I want to be, and I'll keep moving forward no matter what.

Now, it's time for month two.

I'm ready.