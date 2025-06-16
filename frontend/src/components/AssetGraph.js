import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export default function AssetGraph() {

// Sample data
const data = [
  { name: "Jan", Stocks: 400, Crypto: 300 },
  { name: "Feb", Stocks: 300, Crypto: 275 },
  { name: "Mar", Stocks: 200, Crypto: 290 },
  { name: "Apr", Stocks: 278, Crypto: 400 },
  { name: "May", Stocks: 189, Crypto: 390 },
];

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data} margin={{ top: 20, right: 30, left: 0, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="Stocks" stroke="#4CAF50" strokeWidth={2} />
        <Line type="monotone" dataKey="Crypto" stroke="#4CAF50" strokeWidth={2} />
      </LineChart>
    </ResponsiveContainer>
  );
};
