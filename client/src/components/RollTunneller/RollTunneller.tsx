import { Tunneller } from '../../types';
import STYLES from './RollTunneller.module.scss';

type listOfTunnellers = {
    listOfTunnellers: Tunneller[];
    onTunnellerSelected: (tunneller: Tunneller) => void;
}

export const RollTunneller = ({ listOfTunnellers, onTunnellerSelected }: listOfTunnellers) => {

    const setSurnameToUpperCase = (surname: string) => {
        return (surname.startsWith("Mc")) ? "Mc" + surname.slice(2).toUpperCase() : surname.toUpperCase();
    };

    const rollTunneller = listOfTunnellers.map((tunneller) => {

        const handleClick = () => {
            onTunnellerSelected(tunneller);
        };

        return (
            <li className={STYLES.tunneller} key={tunneller.id} onClick={handleClick}>
                <p className={STYLES.surname}>{setSurnameToUpperCase(tunneller.name.surname)}</p>
                <p className={STYLES.forename}>{tunneller.name.forename}</p>
                <p className={STYLES.serial}>{tunneller.serial}</p>
            </li>
        );
        });

    return (
        <>
            {rollTunneller}
        </>
    );

};
