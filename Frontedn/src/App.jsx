import { useState, useEffect } from "react";
import ReactApexChart from "react-apexcharts";

const App = () => {
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/fetch");
        const data = await response.json();
        // Format the data for ApexChart
        const formattedData = data.map((item) => ({
          x: item.date,
          y: [item.open, item.high, item.low, item.close],
        }));
        setChartData([{ data: formattedData }]);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  const options = {
    chart: {
      type: "candlestick",
      height: 350,
    },
    title: {
      text: "Candlestick Chart (OHLC)",
      align: "left",
    },
    xaxis: {
      type: "category",
    },
    yaxis: {
      tooltip: {
        enabled: true,
      },
    },
  };

  return (
    <div id="chart">
      <ReactApexChart
        options={options}
        series={chartData}
        type="candlestick"
        height={350}
      />
    </div>
  );
};

export default App;
