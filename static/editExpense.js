document.addEventListener("DOMContentLoaded", async () => {
  document.getElementById("editExpenseFrom").addEventListener("submit", async (event) => {
    event.preventDefault();
    const id = document.getElementById("expenseId").value;
    const date = document.getElementById("date").value;
    const category = document.getElementById("category").value;
    const description = document.getElementById("description").value;
    const amount = document.getElementById("amount").value;
    const response = await axios.put(`/expenses/edit`, {
      id,
      date,
      category,
      description,
      amount,
    });
    if (response.status === 200) {
      window.location.href = "/expenses";
    }
  });
});
