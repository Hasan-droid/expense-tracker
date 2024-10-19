document.addEventListener("DOMContentLoaded", async () => {
  document.getElementById("editIncomeForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    console.log(`editIncomeForm`);
    const id = document.getElementById("incomeId").value;
    const date = document.getElementById("date").value;
    const category = document.getElementById("category").value;
    const description = document.getElementById("description").value;
    const amount = document.getElementById("amount").value;
    const response = await axios.put(`/incomes/edit`, {
      id,
      date,
      category,
      description,
      amount,
    });
    console.log(response.data);
    if (response.status === 200) {
      window.location.href = "/incomes";
    }
  });
});
