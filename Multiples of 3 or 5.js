function multiples() {
  var sum = 0;

  for (let i = 0; i <= 1000; i++) {
    if (Math.isInteger(i % 15)) {
      sum += i;
    } else if (Math.isInteger(i % 3)) {
      sum += i;
    } else if (Math.isInteger(i % 5)) {
      sum += i;
    }
  }
  console.log(sum);
}


multiples()