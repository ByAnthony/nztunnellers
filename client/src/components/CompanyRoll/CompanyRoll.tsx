import STYLES from './CompanyRoll.module.css';

type Roll = {
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

export const CompanyRoll = ({ roll }: Roll) => {

    const displayTunnellerInfo = (listOfTunnellers: Tunneller[]) => listOfTunnellers.map((tunneller) => {
        return (
            <div key={tunneller.id}>
                <h3>{tunneller.name.forename} {tunneller.name.surname}</h3>
                <p>{tunneller.serial}</p>
            </div>
        );
    });

    const companyRoll = Object.entries(roll).map(([key, listOfTunnellers]) => (
        <div className={STYLES.roll} key={key}>
            <h2>{key}</h2>
            {displayTunnellerInfo(listOfTunnellers)}
        </div>
    ));

    return(
        <>
          {companyRoll}
        </>
    );

};
