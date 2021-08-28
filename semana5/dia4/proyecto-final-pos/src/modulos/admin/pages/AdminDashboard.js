import React from 'react'
import { useSelector } from 'react-redux'
import { Bar } from "react-chartjs-2"
import { format } from "date-fns"

// const data = {
//   labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//   datasets: [
//     {
//       label: '# of Votes',
//       data: [12, 19, 3, 5, 2, 3],
//       backgroundColor: [
//         'rgba(255, 99, 132, 0.2)',
//         'rgba(54, 162, 235, 0.2)',
//         'rgba(255, 206, 86, 0.2)',
//         'rgba(75, 192, 192, 0.2)',
//         'rgba(153, 102, 255, 0.2)',
//         'rgba(255, 159, 64, 0.2)',
//       ],
//       borderColor: [
//         'rgba(255, 99, 132, 1)',
//         'rgba(54, 162, 235, 1)',
//         'rgba(255, 206, 86, 1)',
//         'rgba(75, 192, 192, 1)',
//         'rgba(153, 102, 255, 1)',
//         'rgba(255, 159, 64, 1)',
//       ],
//       borderWidth: 1,
//     },
//   ],
// };

const options = {
  scales: {
    yAxes: [
      {
        ticks: {
          beginAtZero: true,
        },
      },
    ],
  },
};

const AdminDashboard = () => {

  const { platos, cargandoPlatos } = useSelector((state) => state.plato);
  const { pedidosDB } = useSelector((state) => state.pedido);

  let labels = [];
  let precios = [];

  if (platos.length > 0 && pedidosDB.length > 0) {
    labels = pedidosDB.map((objPedidoDB) => {
      let date = new Date(objPedidoDB.pedido_fech);
      return format(date, 'MM/dd hh:mm');
    });
    precios = pedidosDB.map((objPedidoDB) => {
      let total = 0;
      objPedidoDB.pedidoplatos.forEach((objPedidoPlato) => {
        let objPlato = platos.find(
          (plato) => plato.plato_id === objPedidoPlato.plato_id
        );
        total += +objPlato.plato_pre * +objPedidoPlato.pedidoplato_cant;
      });
      return total;
    });
  } 

  console.log(precios);

  const data = {
    labels: labels,
    datasets: [
      {
        label: 'Monto de venta',
        data: precios,
        backgroundColor: ['rgba(255, 99, 132, 0.2)'],
        borderColor: ['rgba(255, 99, 132, 1)'],
        borderWidth: 1
      }
    ]
  }

  return (
    <main className="container">
      <h1 className="display-4 mt-5">
        Dashboard CodiGo - <span className="text-danger">POS</span>
      </h1>
      <hr />
      <div className="row">
        <div className="col-12">
          <Bar data={data} options={options} />
        </div>
      </div>
      <div className="row">
        <div className="col-md-4">
          <div className="card bg-secondary text-white">
            <div className="card-body">
              <h4 className="card-title">PLATOS</h4>
              <h5 className="display-4 text-center">
                {
                  cargandoPlatos ? (<div class="spinner-border text-light" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>) : (platos.length)
                }
              </h5>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card bg-primary text-white">
            <div className="card-body">
              <h4 className="card-title">MESAS</h4>
              <h5 className="display-4 text-center">9</h5>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card bg-dark text-white">
            <div className="card-body">
              <h4 className="card-title">USUARIOS</h4>
              <h5 className="display-4 text-center">15</h5>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}

export default AdminDashboard
