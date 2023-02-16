import { getBanner, getHomeCategoryList, addRadio } from '../../api/common'
import { getIsCommandProductList, getIndexFlashSale, getIndexModuleProductList } from '../../api/product'
import { getAreasList } from '../../api/address'
import { timeData } from '../../utils/countTime'
import Toast from '@vant/weapp/toast/toast'
const app = getApp()
Page({
  data: {
    // bannerList: [
    //   "https://cloud.thorray.com/temp/maicai/banner1.png",
    //   "https://cloud.thorray.com/temp/maicai/banner2.png",
    //   "https://cloud.thorray.com/temp/maicai/banner3.png"
    // ], // 顶部轮播图
    // category: [
    //   {
    //     "id": 1,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg1.png",
    //     "name": "甘蓝"
    //   },
    //   {
    //     "id": 2,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg2.png",
    //     "name": "西红柿"
    //   },
    //   {
    //     "id": 3,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg3.png",
    //     "name": "辣椒"
    //   },
    //   {
    //     "id": 4,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg4.png",
    //     "name": "柠檬"
    //   },
    //   {
    //     "id": 5,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg5.png",
    //     "name": "黄瓜"
    //   }
    // ], // 分类
    // list: [], // 推荐商品列表
    // resultList: [
    //   {
    //     "moduleId": 1,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg5.png",
    //     "name": "甘蓝"
    //   },
    //   {
    //     "moduleId": 2,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg4.png",
    //     "name": "西红柿"
    //   },
    //   {
    //     "moduleId": 3,
    //     "url": "https://cloud.thorray.com/temp/maicai/veg3.png",
    //     "name": "辣椒"
    //   },
    // ], // 分类商品列表
    // saleList: [
    //   {
    //     "id": 1,
    //     "url": "https://cloud.thorray.com/temp/maicai/qiang1.png",
    //     "name": "甘蓝",
    //     "price": "2.5",
    //     "salePrice": "2.1"
    //   },
    //   {
    //     "id": 2,
    //     "url": "https://cloud.thorray.com/temp/maicai/qiang2.png",
    //     "name": "苹果",
    //     "price": "1.5",
    //     "salePrice": "1.1"
    //   },
    //   {
    //     "id": 3,
    //     "url": "https://cloud.thorray.com/temp/maicai/qiang3.png",
    //     "name": "洋葱",
    //     "price": "0.5",
    //     "salePrice": "0.1"
    //   },
    //   {
    //     "id": 4,
    //     "url": "https://cloud.thorray.com/temp/maicai/qiang1.png",
    //     "name": "豆角",
    //     "price": "3.5",
    //     "salePrice": "2.1"
    //   }
    // ],
    countTime: {
      calendar: '', // 相对时间
      duration: '' // 限时抢购倒计时
    },
    radioText: '', // 广播
    topbarStyle: '#fff',
    isNoMore: false,
    _pageNum: 1,
    areaList: [],
    areaIndex: null,
    showPop: false, // 新人领取优惠券
    showLoginBtn: true // 底部登录提示
  },
  async onLoad () {
    try {
      // 获取轮播图 分类 推荐商品
      const [
        { data: { list: bannerList } },
        { data: category },
        // { data: { list: areaList } },
        // { data: { list: saleList, startTime, endTime } },
        // { data }
      ] = await Promise.all([
        getBanner(), // 轮播图
        getHomeCategoryList(), // 分类
        // getAreasList(), // 区域列表
        // getIndexFlashSale(), // 限时抢购
        // addRadio(), // 首页广播
        // // this._getList()
        // this._getModuleList()
      ])
      this.setData({
        // "bannerList": this.data.bannerList,
        bannerList,
        category,
        // areaList: [{ id: null, name: '目前已开放配送范围' }, ...areaList],
        // saleList: saleList || [],
        // countTime: timeData(startTime, endTime),
        // radioText: data ? data.join(' ') : ''
      })
    } catch(err) {
      console.log("index err", err)
    }
    // app.getUserInfo((err, res) => {
    //   // console.log(err, res)
    //   if (!err) {
    //     if (res.canGet) {
    //       this.setData({ showPop: true })
    //     }
    //     if (parseInt(res.cartCount)) {
    //       wx.setTabBarBadge({
    //         index: 2,
    //         text: res.cartCount + ''
    //       })
    //     } else {
    //       wx.removeTabBarBadge({
    //         index: 2
    //       })
    //     }
    //   }
    // })
  },
  // onReady () {
  //   // 获取topbar高度
  //   wx.createSelectorQuery().in(this).select('.topbar').boundingClientRect(rect => {
  //     const { bottom: top } = rect
  //     this.observerContentScroll(-top)
  //   }).exec()
  // },
  onShow () {
    if (parseInt(app.globalData.cartCount)) {
      wx.setTabBarBadge({
        index: 2,
        text: app.globalData.cartCount + ''
      })
    } else {
      wx.removeTabBarBadge({
        index: 2
      })
    }
    // for (let key in app.globalData.cartCountObj) {
    //   const id = parseInt(key)
    //   const index = this.data.list.findIndex(item => item.id === id)
    //   if ((typeof(index) === 'number') && (index != -1)) {
    //     this.setData({
    //       [`list[${index}].cartCount`]: app.globalData.cartCountObj[key]
    //     })
    //   }
    // }
    // this.data.resultList.forEach(res => {
    //   res.productList.forEach(item => {
    //     if (app.globalData.cartCountObj[item.id]) {
    //       item.cartCount = app.globalData.cartCountObj[item.id]
    //     }
    //   })
    // })
    // this.setData({ resultList: this.data.resultList })

    app.getUserInfo((err, res) => {
      // console.log(err, res)
      if(!err) {
        if (res.mobile) {
          if (this.data.showLoginBtn) {
            this.setData({
              showLoginBtn: false
            })
          }
        } else {
          this.setData({
            showLoginBtn: true
          })
        }
      } else {
        this.setData({
          showLoginBtn: true
        })
      }
    })
  },
  // observerContentScroll (top) {
  //   this.createIntersectionObserver().disconnect()
  //   // 设置参考区域减去tobbar高度
  //   // 收缩参照节点布局区域的边界
  //   this.createIntersectionObserver().relativeToViewport({ top })
  //     .observe('.swiper', ({ intersectionRect: { top: intersectionTop } }) => { // 相交区域的上边界坐标
  //       this.setData({
  //         topbarStyle: intersectionTop ? '' : '#fff'
  //       })
  //     })
  // },
  _pickerChange ({ detail: { value } }) {
    // console.log(value)
    this.setData({ areaIndex: value })
  },
  // _getList () {
  //   getIsCommandProductList({ pageNum: this.data._pageNum }, { showLoading: true }).then(({ data }) => {
  //     const list = this.data._pageNum === 1 ? data.list : this.data.list.push(...data.list)
  //     this.setData({
  //       list,
  //       isNoMore: data.isLastPage
  //     })
  //   }).finally(() => {
  //     wx.stopPullDownRefresh()
  //   })
  // },
  _getModuleList () {
    getIndexModuleProductList({ pageNum: this.data._pageNum }, { showLoading: true }).then(({ data }) => {
      this.setData({
        resultList: data
      })
    }).finally(() => {
      wx.stopPullDownRefresh()
    })
  },
  _jumpTo ({ currentTarget: { dataset: { id } } }) {
    // console.log(id)
    wx.navigateTo({ url: `/subPages/product/moduleDetailList/index?id=${id}`})
  },
  _switchClassify ({ currentTarget: { dataset: { id } } }) {
    // console.log(id)
    app.globalData.switchClassifyId = id
    wx.switchTab({
      url: '/pages/classify/index'
    })
  },
  _addSuccess ({ detail }) {
    Toast.success({
      duration: 1000
    })
    // console.log(detail)
    if (parseInt(app.globalData.cartCount)) {
      wx.setTabBarBadge({
        index: 2,
        text: app.globalData.cartCount + ''
      })
    } else {
      wx.removeTabBarBadge({
        index: 2
      })
    }
    // const targetItemIndex = this.data.list.findIndex(item => item.id === detail.id)
    // if ((typeof(targetItemIndex) === 'number') && (targetItemIndex != -1)) {
    //   const key = `list[${targetItemIndex}].cartCount`
    //   this.setData({
    //     [key]: detail.count
    //   })
    // }
    this._setDetailCount(detail)
  },
  _addError ({ detail }) {
    // Toast.fail('添加失败请重试')
    // const targetItemIndex = this.data.list.findIndex(item => item.id === detail.id)
    // if ((typeof(targetItemIndex) === 'number') && (targetItemIndex != -1)) {
    //   const key = `list[${targetItemIndex}].cartCount`
    //   this.setData({
    //     [key]: detail.count
    //   })
    // }
    this._setDetailCount(detail)
  },
  _setDetailCount (detail) {
    const { id, count } = detail
    let indexArr = []
    const arr = this.data.resultList
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr[i].productList.length; j++) {
        if (arr[i].productList[j].id === id) {
          indexArr = [i, j]
          break
        }
      }
    }
    const [i, j] = indexArr
    const key = `resultList[${i}].productList[${j}].cartCount`
    this.setData({
      [key]: count
    })
  },
  _toWebView ({ currentTarget: { dataset: { url } } }) {
    if (url) {
      if (/^(https|http)/.test(url)) {
        wx.navigateTo({ url: `/subPages/other/webPage/index?url=${url}`})
      } else {
        wx.navigateTo({ url })
      }
    }
  },
  _closePop () {
    this.setData({ showPop: false })
  },
  _toGetCoupon () {
    const _this = this
    wx.navigateTo({
      url: '/subPages/coupon/newPerson/index',
      success () {
        _this.setData({ showPop: false })
      }
    })
  },
  _toLogin () {
    wx.navigateTo({ url: '/subPages/login/login/index' })
  },
  // 下拉刷新
  onPullDownRefresh () {
    this.pageNum = 1
    // this._getList()
    this._getModuleList()
  },
  // // 上拉触底事件
  // onReachBottom () {
  //   if (this.data.isNoMore) return
  //   this.data._pageNum = this.data._pageNum + 1
  //   this._getList()
  // },
  onShareAppMessage (res) {
    return {
      title: '彤彤严选',
      path: '/pages/index/index'
    }
  }
})
