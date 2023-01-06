import STYLES from './Roll.module.css';

type Tunnellers = {
    [key: string]: Record<string, Tunneller[]> | never[];
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

export const Roll = ({ tunnellers }: Tunnellers) => {

    const setSurnameToUpperCase = (surname: string) => {
        if (surname.startsWith("Mc")) {
            return "Mc" + surname.slice(2).toUpperCase();
        };
        return surname.toUpperCase();
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

    const companyRoll = Object.entries(tunnellers).map(([key, listOfTunnellers]) => (
        <div id={`letter-${key}`} key={key}>
            <div className={STYLES['letter-container']}>
                <h3 className={STYLES['letter-title']} key={key}>{key}</h3>
            </div>
            <div className={STYLES['tunneller-group']}>
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
