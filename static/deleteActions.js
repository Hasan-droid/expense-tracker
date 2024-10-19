document.addEventListener("DOMContentLoaded", async () => {
  window.deleteExpense = async (expenseId) => {
    const response = await axios.delete(`/expenses?id=${expenseId}`);
    console.log(response.data);
    if (response.status === 200) {
      window.location.reload();
    }
  };
  window.deleteIncome = async (incomeId) => {
    const response = await axios.delete(`/incomes?id=${incomeId}`);
    console.log(response.data);
    if (response.status === 200) {
      window.location.reload();
    }
  };
});
