Component({
  options: {
      addGlobalClass: true,
      multipleSlots: true
  },
  properties: {
      tabIndex: {
          type: Number,
          value: 0
      }
  },
  relations: {
      '../stabs/index': {
          type: 'parent'
      }
  },
  lifetimes: {
      attached: function attached() {}
  },
  methods: {
      calcHeight: function calcHeight(callback) {
          var query = this.createSelectorQuery();
          query.select('.weui-vtabs-content__item').boundingClientRect(function (rect) {
              callback && callback(rect);
          }).exec();
      }
  }
});