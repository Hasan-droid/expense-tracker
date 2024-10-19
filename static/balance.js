document.addEventListener("DOMContentLoaded", async () => {
  const balanceTag = document.querySelector("#balance");
  const fetchData = await axios.get("/balance");
  const balanceData = fetchData.data.balance;
  balanceTag.innerHTML = `Balance: ${balanceData}`;
});
