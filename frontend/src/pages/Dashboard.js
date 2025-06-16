import React, { useState } from "react";
import Header from "../components/Header";
import AssetGraph from "../components/AssetGraph";
import StockAssets from "../components/StockAssets";
import CryptoAssets from "../components/CryptoAssets";


export default function Dashboard() {
  
  return (
    <div className="w-full h-full bg-gray-900 p-3">
        <div className="flex px-12 py-3 flex-col bg-black opacity-95 rounded-xl">

      {/* Header */}
      <Header />
      <div className="p-6 m-6">
        <AssetGraph />
      </div>
      <div className="flex justify-around items-center">

      {/* Page Content */}
      <div className="w-1/3">

      <StockAssets />
      </div>
      <div className="w-1/3">
      <CryptoAssets />

      </div>
      </div>
      <div className="overflow-auto p-3 text-white"></div>
        </div>
    </div>
  );
}
