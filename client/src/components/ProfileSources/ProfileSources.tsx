import type { NominalRoll, NzArchives, Sources } from '../../types/tunneller';
import STYLES from './ProfileSources.module.scss';

type Props = {
    sources: Sources,
}

export function ProfileSources({ sources }: Props) {
  const getNzArchives = (nzArchives: NzArchives[]) => {
    const modifiedArchives = (
      arr: NzArchives[],
      index: number,
      ibid: string,
    ) => arr.slice(index).map((obj) => ({ ...obj, ibid }));
    const newarr = [...modifiedArchives([nzArchives[0]], 0, 'New Zealand Archives Te Rua Mahara o te Kāwanatanga, '), ...modifiedArchives(nzArchives, 1, 'Ibid., ')];
    const italicIbid = (ibid: string) => (ibid === 'Ibid., ' ? <em>{ibid}</em> : ibid);
    return newarr.map((archives) => (
      <p key={archives.reference}>
        {italicIbid(archives.ibid)}
        {archives.reference}
        ,
        {' '}
        <a href={archives.url}>Military Personnel File</a>
        .
      </p>
    ));
  };

  const getNominalRoll = (nominalRoll: NominalRoll) => {
    const title = `${nominalRoll.title}`;
    const volumeRoll = `, ${nominalRoll.volume}, ${nominalRoll.roll}`;
    const reference = `, ${nominalRoll.publisher}, ${nominalRoll.town}, ${nominalRoll.date}, ${nominalRoll.page}.`;
    if (nominalRoll.volume && nominalRoll.roll) {
      return (
        <p>
          <em>{title}</em>
          {volumeRoll}
          {reference}
        </p>
      );
    }
    return (
      <p>
        <em>{title}</em>
        {reference}
      </p>
    );
  };

  return (
    <div className={STYLES.sources}>
      <h4>Sources</h4>
      { getNzArchives(sources.nzArchives) }
      <p>
        Auckland War Memorial Museum Tāmaki Paenga Hira:
        {' '}
        <a href={sources.awmmCenotaph}>Online Cenotaph He Toa Taumata Rau</a>
        .
      </p>
      { getNominalRoll(sources.nominalRoll) }
    </div>
  );
}
