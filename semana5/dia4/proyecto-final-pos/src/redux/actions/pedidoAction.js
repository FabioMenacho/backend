import axios from 'axios';
import { URL_BACKEND } from '../../environments/environments';
import { AGREGAR_PLATO_A_PEDIDO, ELIMINAR_PEDIDO, FIN_CARGANDO_PEDIDOS_BD, INICIO_CARGANDO_PEDIDOS_BD, SET_PEDIDOS_BD } from '../types/types';

const setInicioCargandoPedidosDB = () => ({type: INICIO_CARGANDO_PEDIDOS_BD})
const setFinCargandoPedidosDB = () => ({type: FIN_CARGANDO_PEDIDOS_BD})

export const getPedidoDB = () => {
	return async (dispatch)=>{
		dispatch(setInicioCargandoPedidosDB);

		const endpoint = `${URL_BACKEND}/pedido`;
		const response = await axios.get(endpoint);

		dispatch({
			type: SET_PEDIDOS_BD,
			payload: response.data.pedidos
		})

		dispatch(setInicioCargandoPedidosDB);
	}
}


export const agregarPlatoAction = (objPlato, mesaId) => {
	return {
		type: AGREGAR_PLATO_A_PEDIDO,
		payload: {
			objPlato: objPlato,
			mesaId: mesaId
		}
	};
};

export const eliminarPedidoPorMesaIdAction = (mesaId) => {
	return {
		type: ELIMINAR_PEDIDO,
		payload: mesaId
	};
};
