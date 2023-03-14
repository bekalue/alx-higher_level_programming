#!/usr/bin/node

exports.callMeMoby = function (x, theFuntion) {
  for (let i = 0; i < x; i++) { theFuntion(); }
};
