import type {
  LondonGazette, NominalRoll, NzArchives, Sources,
} from '../../types/tunneller';
import STYLES from './ProfileSources.module.scss';

type Props = {
    sources: Sources,
}

type RecordWithIbid<T> = T & { ibid: string };

export function ProfileSources({ sources }: Props) {
  const getAwmm = (awmmCenotaph: string) => (
    <p>
      Auckland War Memorial Museum Tāmaki Paenga Hira:
      {' '}
      <a href={awmmCenotaph}>Online Cenotaph He Toa Taumata Rau</a>
      .
    </p>
  );

  function addIbid<T extends Record<string, string>>(
    array: T[],
    index: number,
    ibid: string,
  ): RecordWithIbid<T>[] {
    return array.slice(index).map((obj) => ({ ...obj, ibid }));
  }

  const getLondonGazette = (londonGazette: LondonGazette[]) => {
    if (londonGazette.length !== 0) {
      const LondonGazetteList = [...addIbid([londonGazette[0]], 0, 'London Gazette, '), ...addIbid(londonGazette, 1, 'Ibid., ')];
      return LondonGazetteList.map((gazette) => (
        <p key={gazette.page}>
          <em>{gazette.ibid}</em>
          {gazette.date}
          {', '}
          p.&nbsp;
          {gazette.page}
          .
        </p>
      ));
    }
    return null;
  };

  const getNzArchives = (nzArchives: NzArchives[]) => {
    const nzArchivesList = [...addIbid([nzArchives[0]], 0, 'New Zealand Archives Te Rua Mahara o te Kāwanatanga, '), ...addIbid(nzArchives, 1, 'Ibid., ')];
    const italicIbid = (ibid: string) => (ibid === 'Ibid., ' ? <em>{ibid}</em> : ibid);
    return nzArchivesList.map((archives) => (
      <p key={archives.reference}>
        {italicIbid(archives.ibid)}
        {archives.reference}
        {', '}
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
      { getAwmm(sources.awmmCenotaph) }
      { getNzArchives(sources.nzArchives) }
      { getLondonGazette(sources.londonGazette) }
      { getNominalRoll(sources.nominalRoll) }
    </div>
  );
}
