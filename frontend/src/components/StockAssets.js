import React from 'react'

export default function StockAssets() {
    const data = [
        {name: 'Tesla', value: 10000},
        {name: 'Meta', value: 5000},
        {name: 'Exon', value: 15000}
    ]
  return (

    <div className='bg-gray-900 rounded-xl p-6'>
        <div className='pb-3'>
        <h1 className='text-green-500 text-xl text-center pb-4'>Crypto Assets</h1>
        {/* <div className='flex justify-around'> */}
            <div className='text-center'>

        <h2 className='text-green-500 text-xl'>Balance</h2>
        <h3 className='text-green-500 font-bold'>$ {data.reduce((acc, item) => acc + item.value, 0).toLocaleString()}</h3>
            </div>
        {/* </div> */}
        </div>
        <div className='p-1'>
            <ul>
                {data.map((item) => (
                    <li key={item.name} className='flex justify-between text-green-500 py-1'>
                        <p className=''>{item.name}</p>
                        <p className='font-semibold'>$ {item.value.toLocaleString()}</p>
                    </li>
                ))}
            </ul>
        </div>
    </div>
  )
}
