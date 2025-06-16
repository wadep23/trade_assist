import React from 'react'

export default function CryptoAssets() {
    const data = [
        {name: 'Bitcoin', value:300.00},
        {name: 'XRP', value: 600.25},
        {name: 'Etherium', value: 1000.70},
    ]

  return (
    <div className='bg-gray-900 rounded-xl p-6'>
        <div className='pb-3'>
        <h1 className='text-green-500 text-2xl text-center pb-4'>Crypto Assets</h1>
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
