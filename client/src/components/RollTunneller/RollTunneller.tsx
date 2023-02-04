import { Link } from 'react-router-dom';
import STYLES from './RollTunneller.module.scss';
import { Tunneller } from '../../types';

type listOfTunnellers = {
    listOfTunnellers: Tunneller[];
}

export const RollTunneller = ({ listOfTunnellers }: listOfTunnellers) => {

    const rollTunneller = listOfTunnellers.map((tunneller) => {

        return (
            <li className={STYLES.tunneller} key={tunneller.id}>
                <Link to={`/roll/${tunneller.id}`}>
                    <p className={STYLES.surname}>{tunneller.name.surname}</p>
                    <p className={STYLES.forename}>{tunneller.name.forename}</p>
                    <p className={STYLES.serial}>{tunneller.serial}</p>
                </Link>
            </li>
        );
        });

    return (
        <>
            {rollTunneller}
        </>
    );

};
