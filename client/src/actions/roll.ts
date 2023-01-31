const GET_ROLL = 'GET_ROLL';

export const getRoll = (data: any) => {
    return {
        type: GET_ROLL,
        payload: {
            rollData: data
        }
    }
};
