document.addEventListener("DOMContentLoaded", async () => {
  const fetchData = await axios.get("/incomes/bieChart");
  var chartDom = document.getElementById("incomesChart");
  var myChart = echarts.init(chartDom);
  var option;

  option = {
    title: {
      text: "Incomes",
      left: "center",
    },
    tooltip: {
      trigger: "item",
    },
    legend: {
      orient: "vertical",
      left: "left",
    },
    series: [
      {
        name: "Access From",
        type: "pie",
        radius: "50%",
        data: fetchData.data.map((item) => {
          return {
            name: item.category,
            value: item.total,
          };
        }),
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)",
          },
        },
      },
    ],
  };

  option && myChart.setOption(option);
});
