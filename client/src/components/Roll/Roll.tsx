type Props = {
    tunnellers: Array<Tunneller>;
}

type Tunneller = {
    id: number;
    serial: string;
    name: Name;
}

type Name = {
    forename: string;
    surname: string;
}

export const Roll = ({ tunnellers }: Props) => {


    const tunnellersList = tunnellers.map((tunneller: Tunneller, index: number) => {
        return (
            <div key={index}>
                <p>{tunneller.name.forename} {tunneller.name.surname}</p>
                <p>{tunneller.serial}</p>
                <br/>
            </div>
        );
    });

    return(
        <>
          {tunnellersList}
        </>
    );

};
