document.addEventListener("DOMContentLoaded", async () => {
  window.deleteExpense = async (expenseId) => {
    const response = await axios.delete(`/expenses?id=${expenseId}`);
    if (response.status === 200) {
      window.location.reload();
    }
  };
  window.deleteIncome = async (incomeId) => {
    const response = await axios.delete(`/incomes?id=${incomeId}`);
    if (response.status === 200) {
      window.location.reload();
    }
  };
});
