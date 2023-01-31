import { Tunneller } from '../../types';
import { RollTunneller } from '../RollTunneller/RollTunneller';
import STYLES from './Roll.module.scss';

type Tunnellers = {
    tunnellers: Record<string, Tunneller[]> | never[];
    filterByLetter: string;
};

export const Roll = ({ tunnellers, filterByLetter }: Tunnellers) => {

    const tunnellersList = Object.entries(tunnellers);

    const isFilteredByLetter = (letter: string) => {
        return letter === '' ? tunnellersList : tunnellersList.filter((key) => key.includes(letter))
    }

    const companyRoll = isFilteredByLetter(filterByLetter)
        .map(([key, listOfTunnellers]) => (
            <div id={`letter-${key}`} key={key}>
                <div className={STYLES['letter-container']}>
                    <h2 className={STYLES['letter-title']} key={key}>{key}</h2>
                </div>
                <div className={STYLES['tunnellers-container']}>
                    <RollTunneller listOfTunnellers={listOfTunnellers} />
                </div>
            </div>
        ));

    return(
        <div className={STYLES.roll}>
          {companyRoll}
        </div>
    );

};
