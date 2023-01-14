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
            <a href='./' className={STYLES.tunneller} key={tunneller.id}>
                <p className={STYLES.surname}>{setSurnameToUpperCase(tunneller.name.surname)}</p>
                <p className={STYLES.forename}>{tunneller.name.forename}</p>
                <p className={STYLES.serial}>{tunneller.serial}</p>
            </a>
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
                    <h2 className={STYLES['letter-title']} key={key}>{key}</h2>
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
