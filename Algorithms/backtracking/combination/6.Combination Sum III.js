const combinationSum3 = (k, n) => {
  const res = []

  const dfs = (start, path, sum) => {
    if (path.length === k && sum === n) {
      res.push(path.slice());
      return;
    }

    for (let i = start; i < n; i++) {
      path.push(i);
      dfs(i + 1, path, sum + i);
      path.pop();
    }
  }
  dfs(1, [], 0);
  return res;
}

console.log(combinationSum3(3, 7)); // [[1,2,4]]
