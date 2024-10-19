const generateTable = async () => {
  const dateFilter = document.querySelector("#dateFilter");
  const categoryFilter = document.querySelector("#categoryFilter");
  const tableBody = document.querySelector("#expenseTable");
  const responseData = await axios.get(`/filter?date=${dateFilter.value}&category=${categoryFilter.value}`);
  const expenses = responseData.data.expenses;
  tableBody.innerHTML = "";
  expenses.forEach((expense) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${expense.date}</td>
      <td>${expense.category}</td>
      <td>${expense.description}</td>
      <td>${expense.amount}</td>
       <td>
            <button class="btn btn-danger" onclick="deleteExpense(${expense.id})">Delete</button>
            <a href="/expenses/edit?id=${expense.id}" class="btn btn-warning">Edit</a>
          </td>
      `;
    tableBody.appendChild(tr);
  });
};
document.addEventListener("DOMContentLoaded", () => {
  const dateFilter = document.querySelector("#dateFilter");
  const categoryFilter = document.querySelector("#categoryFilter");
  dateFilter.addEventListener("input", generateTable);
  categoryFilter.addEventListener("input", generateTable);
});
