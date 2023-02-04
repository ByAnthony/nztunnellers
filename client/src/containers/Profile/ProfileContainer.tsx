import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';

export const ProfileContainer = () => {
  const { id } = useParams();
  const tunneller = useGetTunnellerByIdQuery(Number(id!));

  return (
    <div>
      {tunneller.data?.name === undefined ? 'not found' : tunneller.data.name.forename + tunneller.data.name.surname}
    </div>
  );
};
