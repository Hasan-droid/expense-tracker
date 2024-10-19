const generateTable = async () => {
  const dateFilter = document.querySelector("#dateFilter");
  const categoryFilter = document.querySelector("#categoryFilter");
  const tableBody = document.querySelector("#incomeTable");
  const responseData = await axios.get(`/filter/income?date=${dateFilter.value}&category=${categoryFilter.value}`);
  const incomes = responseData.data.income;
  console.log(incomes);
  tableBody.innerHTML = "";
  incomes.forEach((income) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
        <td>${income.date}</td>
        <td>${income.category}</td>
        <td>${income.description}</td>
        <td>${income.amount}</td>
         <td>
              <button class="btn btn-danger" onclick="deleteIncome(${income.id})">Delete</button>
              <a href="/incomes/edit?id=${income.id}" class="btn btn-warning">Edit</a>
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
