import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { RollService } from '../../services/RollService';

export const TunnellerProfile = () => {

  const { id } = useParams();
  const [tunneller, setTunneller] = useState();

  useEffect(() => {
    RollService.getTunneller(Number(id))
    .then(data => setTunneller(data))
  });

  return (
    <div>
     test
    </div>
  );
}
