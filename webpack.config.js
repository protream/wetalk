var path = require('path')
var webpack = require('webpack')
var ManifestPlugin = require('webpack-manifest-plugin')
var CleanWebpackPlugin = require('clean-webpack-plugin')
var ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  entry: {
    main: './assets/js/main.js',
    common: [
      'vue',
      'axios',
      'jquery/src/jquery.js',
      'bootstrap/dist/js/bootstrap.js',
      'bootstrap/dist/css/bootstrap.css'
    ]
  },

  output: {
    path: path.resolve(__dirname, './wetalk/static/dist/'),
    filename: 'js/[name].[chunkhash:8].js',
  },

  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: { extractCSS: true }
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader'
        })
      },
      {
        test: /\.less$/,
        use: ExtractTextPlugin.extract({
          fallback: 'css-loader',
          use: 'less-loader'
        })
      },
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: 'images/[name].[hash:8].[ext]'
        }
      },
      {
        test: /\.(eot|ttf|woff|woff2)$/,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[hash:8].[ext]'
        }
      }
    ]
  },

  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    }
  },

  plugins: [
    new ManifestPlugin(),
    new CleanWebpackPlugin(['wetalk/static/dist']),
    new webpack.optimize.CommonsChunkPlugin({
      name: 'common',
      filename: 'js/common.[chunkhash:8].js'
    }),
    new ExtractTextPlugin({
      filename: 'css/[name].[chunkhash:8].css',
      allChunks: true
    })
  ]
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production')
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: false,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    }),
  ])
}
