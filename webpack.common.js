const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
  entry: {
    main: './frontend/main.js'
  },
  module: {
    rules: [{
      test: /\.scss$/,
      use: [
        MiniCssExtractPlugin.loader,
        'css-loader',
        'sass-loader',
        'postcss-loader'
      ]
    }, {
      test: /\.(eot|otf|ttf|woff|woff2|svg)$/,
      use: {
        loader: 'file-loader',
        options: {
          name: 'assets/[name].[ext]'
        }
      }
    }, {
      test: /\.(png|jpg|jpeg)$/,
      use: {
        loader: 'file-loader',
        options: {
          name: 'images/[name].[ext]'
        }
      }
    }]
  },
  plugins: [new MiniCssExtractPlugin({
    filename: '[name].css'
  })],
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'src/djangolango/static/djangolango'),
  }
};