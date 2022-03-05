Grid.prototype.monotonicity2 = function() {
    // scores for all four directions
    var totals = [0, 0, 0, 0];
  
    // up/down direction
    for (var x=0; x<4; x++) {
      var current = 0;
      var next = current+1;
      while ( next<4 ) {
        while ( next<4 && !this.cellOccupied( this.indexes[x][next] )) {
          next++;
        }
        if (next>=4) { next--; }
        var currentValue = this.cellOccupied({x:x, y:current}) ?
          Math.log(this.cellContent( this.indexes[x][current] ).value) / Math.log(2) :
          0;
        var nextValue = this.cellOccupied({x:x, y:next}) ?
          Math.log(this.cellContent( this.indexes[x][next] ).value) / Math.log(2) :
          0;
        if (currentValue > nextValue) {
          totals[0] += nextValue - currentValue;
        } else if (nextValue > currentValue) {
          totals[1] += currentValue - nextValue;
        }
        current = next;
        next++;
      }
    }
  
    // left/right direction
    for (var y=0; y<4; y++) {
      var current = 0;
      var next = current+1;
      while ( next<4 ) {
        while ( next<4 && !this.cellOccupied( this.indexes[next][y] )) {
          next++;
        }
        if (next>=4) { next--; }
        var currentValue = this.cellOccupied({x:current, y:y}) ?
          Math.log(this.cellContent( this.indexes[current][y] ).value) / Math.log(2) :
          0;
        var nextValue = this.cellOccupied({x:next, y:y}) ?
          Math.log(this.cellContent( this.indexes[next][y] ).value) / Math.log(2) :
          0;
        if (currentValue > nextValue) {
          totals[2] += nextValue - currentValue;
        } else if (nextValue > currentValue) {
          totals[3] += currentValue - nextValue;
        }
        current = next;
        next++;
      }
    }
  
    return Math.max(totals[0], totals[1]) + Math.max(totals[2], totals[3]);
  }
  