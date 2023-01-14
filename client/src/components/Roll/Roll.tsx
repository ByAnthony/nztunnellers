import STYLES from './Roll.module.scss';

type Tunnellers = {
    tunnellers: Record<string, Tunneller[]> | never[];
    filterByLetter: string;
};

type Tunneller = {
    id: number;
    serial: string;
    name: Name;
};

type Name = {
    forename: string;
    surname: string;
};

export const Roll = ({ tunnellers, filterByLetter }: Tunnellers) => {

    const setSurnameToUpperCase = (surname: string) => {
        return (surname.startsWith("Mc")) ? "Mc" + surname.slice(2).toUpperCase() : surname.toUpperCase();
    };

    const displayTunnellerInfo = (listOfTunnellers: Tunneller[]) => listOfTunnellers.map((tunneller) => {
        return (
            <div className={STYLES.tunneller} key={tunneller.id}>
                <h3 className={STYLES.surname}>{setSurnameToUpperCase(tunneller.name.surname)}</h3>
                <h4 className={STYLES.forename}>{tunneller.name.forename}</h4>
                <p className={STYLES.serial}>{tunneller.serial}</p>
            </div>
        );
    });

    const tunnellersList = Object.entries(tunnellers);

    const isFilteredByLetter = (letter: string) => {
        return letter === '' ? tunnellersList : tunnellersList.filter((key) => key.includes(letter))
    }

    const companyRoll = isFilteredByLetter(filterByLetter)
        .map(([key, listOfTunnellers]) => (
            <div id={`letter-${key}`} key={key}>
                <div className={STYLES['letter-container']}>
                    <h3 className={STYLES['letter-title']} key={key}>{key}</h3>
                </div>
                <div className={STYLES['tunnellers-container']}>
                    {displayTunnellerInfo(listOfTunnellers)}
                </div>
            </div>
        ));

    return(
        <div className={STYLES.roll}>
          {companyRoll}
        </div>
    );

};
