#!/usr/bin/node

module.exports = class Rectangle {
  constructor(widthValue, heightValue) {
    if (widthValue > 0 && heightValue > 0) {
      [this.width, this.height] = [widthValue, heightValue];
    }
  }
};

