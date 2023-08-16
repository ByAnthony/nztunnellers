import { Name } from '../../types/roll';
import STYLES from './Title.module.scss';

type TwoLineTitleProps = {
  title: string | undefined;
  name: Name | undefined;
}

type SubTitleProps = {
  subTitle: number | string;
}

type Props = {
  title?: string;
  name?: Name;
  subTitle: number | string;
}

function TwoLineTitle({ title, name }: TwoLineTitleProps) {
  const isTitle = (string: string) => {
    const [titleLine1, titleLine2] = string.split('\\');
    return [titleLine1, titleLine2];
  };

  return (
    <h1>
      <span className={STYLES['title-line-1']}>{ title ? isTitle(title)[0] : name?.forename }</span>
      <span className={STYLES['title-line-2']}>{ title ? isTitle(title)[1] : name?.surname }</span>
    </h1>
  );
}

function SubTitle({ subTitle }: SubTitleProps) {
  return <p className={STYLES['title-line-3']}>{ typeof subTitle === 'string' ? subTitle : `Chapter ${subTitle}`}</p>;
}

export function Title({ title, name, subTitle }: Props) {
  return (
    <>
      <div className={STYLES['main-title']}>
        <TwoLineTitle title={title} name={name} />
      </div>
      <SubTitle subTitle={subTitle} />
    </>
  );
}

Title.defaultProps = {
  title: null,
  name: null,
};
