document.addEventListener("DOMContentLoaded", async () => {
  const fetchData = await axios.get("/barChart");
  const data = fetchData.data;
  var chartDom = document.getElementById("barChart");
  var myChart = echarts.init(chartDom);
  var option;

  option = {
    title: {
      text: "Expenses",
      subtext: "Total expenses per month",
      left: "center",
    },
    xAxis: {
      type: "category",
      data: data.map((item) => item.date),
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: data.map((item) => item.total),
        type: "bar",
      },
    ],
  };

  option && myChart.setOption(option);
});
